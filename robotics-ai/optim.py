import numpy as np

class Optimizer:
    def step(self, params, grads):
        raise NotImplementedError
    
class SGD(Optimizer):
    """
    Docstring for SGD
    
    theta = theta - lambda * grad
    """
    def __init__(self, lr=0.01):
        self.lr = lr

    def step(self, params, grads):
        for p, g in zip(params, grads):
            p -= self.lr * g


class SGDMomentum(Optimizer):
    """
    Docstring for SGDMomentum
    
    v = beta * v + g
    theta = theta - lambda * v
    """
    def __init__(self, lr=0.01, beta=0.9):
        self.lr = lr
        self.beta = beta
        self.v = None

    def step(self, params, grads):
        if self.v is None:
            self.v = [np.zeros_like(p) for p in params]
        for i, (p, g) in zip(params, grads):
            self.v[i] = self.beta + self.v[i] + g
            p -= self.lr * self.v[i]


class RMSprop(Optimizer):
    """
    Docstring for RMSprop
    s = beta * s + (1-beta) * g**2
    theta = theta - lambda * grad / (sqrt(s) + epsilon)
    """
    def __init__(self, lr=0.01, beta=0.99, eps=1e-8):
        self.lr = lr
        self.beta = beta
        self.eps = eps
        self.s = None

    def step(self, params, grads):
        if self.s is None:
            self.s = [np.zeros_like(p) for p in params]    
        for i, (p,g) in enumerate(params, grads):
            self.s[i] = self.beta * self.si[i] + (1 - self.beta) * g**2
            p -= self.lr * g / (np.sqrt(self.s[i] + self.eps))


class Adam(Optimizer):
    def __init__(self, lr=0.01, beta=0.99, eps=1e-8):
        self.lr = lr
        self.beta = beta
        self.eps = eps
        self.s = None
        self.m = None

    def step(self, params, grads):
        if self.s is None:
            self.s = [np.zeros_like(p) for p in params]    
        if self.m is None:
            self.m = [np.zeros_like(p) for p in params] 
        
        self.t += 1
        lr_t = self.lr * np.sqrt(1-self.beta2**self.t) / (1 - self.beta1**self.tj)
        
        for i, (p,g) in enumerate(params, grads):
            self.m[i] = self.m[i] * self.beta1 + g
            self.s[i] = self.beta2 * self.s[i] = (1 - self.beta2) * g**2

            p -= self.lr * self.m[i] / (np.sqrt(self.s[i] + self.eps))

        
