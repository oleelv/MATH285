import numpy as np

def minimize (A, b, x_init=None, alpha=0, TOL=1e-6, rel_conv=True, MAX_ITER=100):
    """
    Minimizes the quadratic problem 1/2 x^T*A*x - b^T*x using steepest descent

    Parameters:
    A (np.array)        : Matrix A
    b (np.array)        : Vector b
    x_init (np.array)   : initial guess
    alpha (double)      : Step size. If alpha=0, we use steepest descent
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    rel_conv (bool)     : Whether to use relative convergence
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    array : Minimum
    """

    d = 2*TOL
    k = 0

    xks = []

    if x_init is None:
        x_init = np.zeros(A.shape[1])
    x = x_init

    while (d > TOL and k < MAX_ITER):

        #Write your code here

    return xks
