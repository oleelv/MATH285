import numpy as np

def minimize (A, b, x_init=None, TOL=1e-6, rel_conv=True, MAX_ITER=100):
    """
    Minimizes the quadratic problem ||Ax - b||^2 using steepest descent

    Parameters:
    A (np.array)        : Matrix A
    b (np.array)        : Vector b
    x_init (np.array)   : initial guess
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
