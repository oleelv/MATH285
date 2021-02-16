import numpy as np

def solve (grad_f, hess_f, x_init=None, TOL=1e-6, rel_conv=True,
        gamma=1,MAX_ITER=100):
    """
    Minimizes f(x) over Rn using Newton's method

    Parameters:
    grad_f (function)   : Gradient of f
    hess_f (function)   : Hessian of f
    x_init (np.array)   : initial guess
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    rel_conv (bool)     : Whether to use relative convergence
    gamma (double)      : Damping of update step (0,1]
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    array : Minimum
    """

    d = 2*TOL
    k = 0

    xks = []

    if x_init is None:
        x_init = np.zeros(grad_f.shape[0])
    x = x_init

    xks.append(x)

    while (d > TOL and k < MAX_ITER):

        #Write your code here

    return xks


def solve_nls (grad_f, hess_f, data, x_init=None, TOL=1e-6, rel_conv=True,
        gamma=1,MAX_ITER=100):
    """
    Minimizes the non-linear least squares problem ||Ax - b||^2 using Newton's method

    Parameters:
    grad_f (function)   : Gradient of f
    hess_f (function)   : Hessian of f
    data (np.array)     : 2d-array with data points (ti, yi)
    x_init (np.array)   : initial guess
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    rel_conv (bool)     : Whether to use relative convergence
    gamma (double)      : Damping of update step (0,1]
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    array : Minimum
    """

    d = 2*TOL
    k = 0

    xks = []

    t = data[0,:]
    y = data[1,:]

    if x_init is None:
        x_init = np.zeros(grad_f.shape[0])
    x = x_init

    xks.append(x)

    while (d > TOL and k < MAX_ITER):

        #Write your code here (This is very similar to the function above)

    return xks
