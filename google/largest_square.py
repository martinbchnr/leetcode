import numpy as np


arr = np.array([[0,1,1,0,1],
                [1,1,0,1,0],
                [0,1,1,1,0],
                [1,1,1,1,0],
                [1,1,1,1,1],
                [0,0,0,0,0]])

def largest_square(arr: np.ndarray) -> int:
    """
    Function computing the area of the largest contained square consisting of just ones
    """
    
    mem = np.zeros_like(arr)
    n, m = arr.shape
    max_d = 0
    
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):

            if arr[i][j] == 0:
                continue

            if mem[i][j] != 0:
                continue

            down = arr[i+1][j]
            right = arr[i][j+1]

            # start recursion
            if down == 1 and right == 1:
                d = recurse_sq(arr[i+1:][j+1:], 1)
                if arr[i+d][j+d] == 1:
                    mem[i:i+d,j:j+d] = d
                    if d > max_d:
                        max_d = d
            else:
                continue

    return max_d * max_d


def recurse_sq(arr, d):
    n = arr.shape[0]
    m = arr.shape[1]

    sq_dim = min(n,m)

    if sq_dim == 1:
        if arr[0][0] == 1:
            return d+1
        else:
            return d
    
    for i in range(sq_dim):
        for j in range(sq_dim):

            # down = arr[i+1][j]
            # right = arr[i][j+1]

            if arr[i+1][j] + arr[i][j+1] == 2:
                recurse_sq(arr[i+1:][j+1:], d+1)
            else:
                return d
            


