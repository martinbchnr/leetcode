import torch
import torch.nn as nn
import math


class SelfAttentionLayer(nn.Module):
    def __init__(self, d_model: int):
        # d_model: dimensionality of the input embeddings
        super().__init__()
        self.d_model = d_model

        # Three linear projections — no bias needed (common in practice)
        self.W_q = nn.Linear(d_model, d_model, bias=False)
        self.W_k = nn.Linear(d_model, d_model, bias=False)
        self.W_v = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # x: (batch, seq_len, d_model)

        Q = self.W_q(x)   # (batch, seq_len, d_model)
        K = self.W_k(x)   # (batch, seq_len, d_model)
        V = self.W_v(x)   # (batch, seq_len, d_model)

        # Scaled dot-product: QK^T / sqrt(d_model)
        scale = math.sqrt(self.d_model)
        scores = torch.matmul(Q, K.transpose(-2, -1)) / scale
        # scores: (batch, seq_len, seq_len)

        attn_weights = torch.softmax(scores, dim=-1)
        # attn_weights[i, j] = how much token i attends to token j

        # Weighted sum of values
        out = torch.matmul(attn_weights, V)
        # out: (batch, seq_len, d_model)

        return out, attn_weights
    

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, h):
        super().__init__()
        assert d_model % h == 0
        self.h = h
        self.d_k = d_model // h          # size of each slice

        self.W_q = nn.Linear(d_model, d_model, bias=False)
        self.W_k = nn.Linear(d_model, d_model, bias=False)
        self.W_v = nn.Linear(d_model, d_model, bias=False)
        self.W_o = nn.Linear(d_model, d_model, bias=False)

    def forward(self, x):
        B, S, D = x.shape

        # Project then slice into h heads
        Q = self.W_q(x).view(B, S, self.h, self.d_k).transpose(1, 2)
        K = self.W_k(x).view(B, S, self.h, self.d_k).transpose(1, 2)
        V = self.W_v(x).view(B, S, self.h, self.d_k).transpose(1, 2)
        # shape: (B, h, S, d_k)

        scores = Q @ K.transpose(-2, -1) / math.sqrt(self.d_k)
        attn = torch.softmax(scores, dim=-1)
        out = attn @ V
        # shape: (B, h, S, d_k)

        # Concatenate heads and project
        out = out.transpose(1, 2).contiguous().view(B, S, D)
        return self.W_o(out)
    

class PositionalEncoding(nn.Module):
    """
    PE(pos, 2i)   = sin(pos / 10000^(2i/d_model))
    PE(pos, 2i+1) = cos(pos / 10000^(2i/d_model))
    """
    def __init__(self, d_model, max_seq_len=512):
        super().__init__()

        pe = torch.zeros(max_seq_len, d_model)
        pos = torch.arange(0, max_seq_len).unsqueeze(1)      # (S, 1)
        div = torch.exp(
            torch.arange(0, d_model, 2) * -(math.log(10000) / d_model)
        )                                                      # (d_model/2,)

        pe[:, 0::2] = torch.sin(pos * div)   # even dims
        pe[:, 1::2] = torch.cos(pos * div)   # odd dims

        self.register_buffer('pe', pe.unsqueeze(0))  # (1, S, d_model)

    def forward(self, x):
        # x: (B, S, d_model)
        return x + self.pe[:, :x.size(1)]
    
class FeedForward(nn.Module):
    def __init__(self, d_model, d_ff, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(d_ff, d_model),
        )

    def forward(self, x):
        return self.net(x)   # (B, S, d_model) → (B, S, d_model)
    
class EncoderBlock(nn.Module):
    def __init__(self, d_model, h, d_ff, dropout=0.1):
        super().__init__()

        self.attn      = MultiHeadAttention(d_model, h)
        self.ff        = FeedForward(d_model, d_ff, dropout)

        self.norm1     = nn.LayerNorm(d_model)
        self.norm2     = nn.LayerNorm(d_model)

        self.dropout   = nn.Dropout(dropout)

    def forward(self, x):
        # --- Sublayer 1: Multi-Head Attention ---
        # Pre-norm: normalize x before attention (modern convention)
        x = x + self.dropout(self.attn(self.norm1(x)))

        # --- Sublayer 2: Feed-Forward ---
        x = x + self.dropout(self.ff(self.norm2(x)))

        return x  # (B, S, d_model)


class TransformerEncoder(nn.Module):
    def __init__(self, vocab_size, d_model, h, d_ff,
                 n_layers, max_seq_len, dropout=0.1):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_enc   = PositionalEncoding(d_model, max_seq_len)
        self.dropout   = nn.Dropout(dropout)

        self.layers    = nn.ModuleList([
            EncoderBlock(d_model, h, d_ff, dropout)
            for _ in range(n_layers)
        ])

        self.norm      = nn.LayerNorm(d_model)  # final norm

    def forward(self, x):
        # x: (B, S) token indices
        x = self.dropout(self.pos_enc(self.embedding(x)))

        for layer in self.layers:
            x = layer(x)

        return self.norm(x)  # (B, S, d_model)
    

class DecoderBlock(nn.Module):
    """
    The decoder is like the encoder but with two key additions — it needs to both generate output tokens and attend to the encoder's output. It has three sublayers instead of two:
    output tokens (shifted right)
        ↓
    Embedding + Positional Encoding
        ↓
    ┌─────────────────────────────────┐
    │  1. Masked Self-Attention       │  ← attends to previous output tokens only
    │  2. Cross-Attention             │  ← attends to encoder output
    │  3. Feed-Forward                │  ← same as encoder
    └─────────────────────────────────┘
        × N layers
        ↓
    Linear + Softmax  →  probability over vocab
    
    Sublayer 1 — Masked self-attention
    Same as the encoder's self-attention, but with a causal mask applied. When generating token at position t, the model must not see future tokens — so you mask out all positions > t by setting those attention scores to -inf before softmax, making their weights zero:
    pythonmask = torch.triu(torch.ones(S, S), diagonal=1).bool()
    scores = scores.masked_fill(mask, float('-inf'))
    """
    def __init__(self, d_model, h, d_ff, dropout=0.1):
        super().__init__()
        self.self_attn  = MultiHeadAttention(d_model, h)  # masked
        self.cross_attn = MultiHeadAttention(d_model, h)  # Q from decoder, K/V from encoder
        self.ff         = FeedForward(d_model, d_ff, dropout)

        self.norm1  = nn.LayerNorm(d_model)
        self.norm2  = nn.LayerNorm(d_model)
        self.norm3  = nn.LayerNorm(d_model)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, encoder_out, mask=None):
        # 1. masked self-attention
        x = x + self.dropout(self.self_attn(self.norm1(x), mask=mask))

        # 2. cross-attention — Q from x, K/V from encoder
        x = x + self.dropout(self.cross_attn(self.norm2(x), encoder_out))

        # 3. feed-forward
        x = x + self.dropout(self.ff(self.norm3(x)))

        return x