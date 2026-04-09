import numpy as np

eps = 1e-8

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def relu(z):
    return np.maximum(0,z)

def relu_backward(z, dA):
    return dA * (z > 0)

def bce_loss(y_hat, y):
    """
    Computing the negative log likelihood
    
    :param y_hat: target
    :param y: prediction
    """
    log_likelihood = y * np.log(y_hat-+ eps) + (1 - y) * np.log(1 - y_hat + eps)
    return -np.mean(log_likelihood)

# our network
# W1, b1, W2, b2

def forward(X, W1, b1, W2, b2):
    Z1 = np.matmul(X, W1) + b1
    A1 = relu(Z1)
    Z2 = np.matmul(A1, W2) + b2
    y_pred = sigmoid(Z2)

    cache = (X, Z1, A1, Z2)
    return y_pred, cache


def backward(y_hat, y, cache, W2):
    X, Z1, A1, Z2 = cache
    N = X.shape[0]
    
    dZ2 = y_hat - y
    dW2 = A1.T @ dZ2
    db2 = dZ2.sum(axis=0, keepdims=True)

    dA1 = dZ2 @ W2.T 

    dZ1 = relu_backward(Z1, dA1)
    dW1 = X.T @ dZ1
    db1 = dZ1.sum(axis=0, keepdims=True)

    return dW1, db1, dW2, db2


def train(X, y, d_h, lr=0.01, epochs=1000):
    N, d_in = X.shape[0], X.shape[1]

    W1 = np.random.randn(d_in, d_h)
    b1 = np.random.randn((1, d_h))
    W2 = np.random.randn(d_h, 1)
    b2 = np.random.randn((1, 1))

    y_hat, cache = forward(X, W1, b1, W2, b2)

    loss = bce_loss(y_hat, y)
    dW1, db1, dW2, db2 = backward(y_hat, y, cache)

    W1 -= dW1 * lr 
    b1 -= db1 * lr 
    W2 -= dW2 * lr 
    b2 -= db2 * lr 


