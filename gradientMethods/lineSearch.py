import numpy as np

def _backtracking(f, xk, dk, c, tau):
    """
    Apply backtracking line search according to Armijo rule

    Parameters:
    f (function)        : cost functional
    xk (np.array)       : iterate k
    dk (np.array)       : search direction
    c (double)          : constant in Armijo rule
    tau (double)        : reduction parameter in backtracing

    Returns:
    alpha (double)      : step length
    """
    alpha = 1

    gk = - dk
    
    while f(xk + alpha*dk) > f(xk) + c*alpha*dk.dot(gk):
        alpha = tau*alpha
  
    print('The value of alpha is:', alpha)
    return alpha


def minimize (f, grad_f, dim=1, x_init=None, c=1, tau=.5, TOL=1e-6, rel_conv=True, MAX_ITER=100):
    """
    Minimizes f(x) using gradient descent with backtracking line search

    Parameters:
    f (function)        : cost functional
    grad_f (function)   : gradient of cost functional
    dim (int)           : dimension of x
    x_init (np.array)   : initial guess
    tau (double)        : reduction parameter in backtracking
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    rel_conv (bool)     : Whether to use relative convergence
    MAX_ITER (int)      : Maximal number of iterations

    Returns:
    array : Minimum
    """

    C = 10e-2

    d = 2*TOL
    k = 0

    xks = []

    if x_init is None:
        x_init = np.zeros(dim)
    x = x_init

    while (d > TOL and k < MAX_ITER):
        xp = x

        #Compute grad f(x)
        gk = grad_f(xp)
        
        #Search direction
        dk = - gk
        
        #Find inexact step length
        ak = _backtracking(f, xp, dk, c, tau)

        #Update xk
        x = xp + ak*dk
        xks.append(x)
        
        #Update change
        if rel_conv and k > 0:
            d = np.linalg.norm(x - xp) / np.linalg.norm(xp)
        else:
            d = np.linalg.norm(x - xp)
        k = k+1

    return xks
