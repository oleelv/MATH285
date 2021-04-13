import numpy as np

def _enteringIndex(NP, sn, rule='Dantzig'):
    """
    Function that decides which index is the enter the basis at each step
    """
    if rule == 'Dantzig':
        return np.argmin(sn)

def _phaseI(A, b):
    """
    Function that finds a basic feasible solution in the Simplex method, i.e.
    the Phase I-algorithm.

    Parameters:
    A (np.array)  : Coefficient matrix
    b (np.array)  : Coefficient vector

    Returns:
    BP (list)       : Index of feasible basis
    xb (np.array)   : Basic feasible solution
    """
    m, n = A.shape

    I = np.eye(m)
    AI = np.concatenate((A,I),axis=1)
    c = np.concatenate((np.zeros(n),np.ones(m)))

    NP = [x for x in range(0,n,1)]
    BP = [x for x in range(n,m+n,1)]

    return _compute(AI, b, c, BP, NP)


def _phaseII(A, b, c, BP, NP):
    """
    Function that finds an optimal solution using the Simplex method, i.e.
    the Phase II-algorithm.

    Parameters:
    A (np.array)    : Coefficient matrix
    b (np.array)    : Coefficient vector
    c (np.array)    : Cost vector
    BP (list)       : Index basis of initial feasible set
    NP (list)       : Complement of BP

    Returns:
    BP (list)       : Index of optimal feasible basis
    xb (np.array)   : Optimal solution
    """

    return _compute(A, b, c, BP, NP)

def _compute(A, b, c, BP, NP, MAX_ITER=100):

    #Write your code here (Implement the simplex algorithm)

def solve(A, b, c, MAX_ITER=100):
    """
    Solve linear programs of standard form using the (revised) Simplex method.
    That is, we solve min c^T*x subject to Ax = b, x >= 0.

    Parameters:
    A (np.array)   : Coefficient matrix
    c (np.array)   : Cost vector

    Returns:
    np.array: Solution x^* of the problem
    """
    m, n = A.shape

    # Phase I of Simplex method: Find a basic feasible solution
    [BP, xb] = _phaseI(A, b)
    NP = [x for x in range(n) if x not in BP]

    # Phase II of Simplex method: Find an optimal solution
    [BP, xb] = _phaseII(A, b, c, BP, NP)

    return xb
