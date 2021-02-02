import numpy as np

def minimize (A, b, x_init=None, TOL=1e-6, rel_conv=True, MAX_ITER=100):
    """
    Solves Ax = b by conjugate gradient method (i.e. we minimize
    1/2 xT*A*x - xT*b)

    Parameters:
    A (np.array)        : Matrix A
    b (np.array)        : Vector b
    x_init (np.array)   : initial guess
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    rel_conv (bool)     : Wheter to use relative convergence
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    array : Minimum
    """

    e = 2*TOL
    k = 0

    MAX_ITER = min(MAX_ITER, A.shape[0])

    if x_init is None:
        x_init = np.zeros(A.shape[0])
    xk = x_init
    gk = A.dot(xk) - b

    if np.linalg.norm(gk) == 0:
        return xk, k
    else:
        dk = -gk

    while (k < MAX_ITER):

        #Write your code here

    return xk, k
