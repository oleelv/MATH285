def solve (f_deriv, f_dderiv, x_init=0, TOL=1e-6, MAX_ITER=1000, verbose=0):
    """
    Solve one-dimensional minimization problem using Newton's method.

    Parameters:
    f_deriv (function)  : Derivative of f
    f_dderiv (function) : Second derivative of f
    x_init (double)     : Initial guess of minimum
    TOL (double)        : Stopping tolerance of ||x_{k+1} - x_k||
    MAX_ITER (int)      : Maximal number of iterations
    verbose (0/1)       : Whether to print information

    Returns:
    double: Minimum
    """
    xk = x_init
    k = 0
    # Check if we by some amazing luck already found the solution
    if f_deriv(xk) == 0:
        print("The initial guess was actually minimum!")
        return xk

    while (k < MAX_ITER):

        #Write your code here

        if verbose == 1:
            print("After {} iteration(s), the estimate xk = {}".format(k, xk))

    print("Maximum is reached! The estimate of the minimmum is : {}".format(xk))
    return xk # maximum iteration reached
