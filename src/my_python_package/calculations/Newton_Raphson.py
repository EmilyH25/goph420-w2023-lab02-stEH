import numpy as np

def root_newton_raphson(x0,freq,f,dfdx,eps_s=1e-8):
    """implements the newton-raphson root finding method for a provided equation

    Parameters
    ----------
    x0 : float
        The initial guess value for the root
    freq : float
        Provided value for the frequency
    f : function
        The function for which the root must be calculated
    dfdx : function
        The derivative of the function for which the root will be calculated
    eps_s : float
        The desired stopping criterion for the function. Default value provided.

    Returns
    -------
    float
        The estimated root of the function
    integer
        The number of iterations required to reach the stopping criterion
    list
        A list containing the error values for each iteration
    """
    
    # initializing conditions for the newton-raphson method
    eps_a = 2*eps_s
    xk = x0
    error = []
    niter = 0
    d = []
    
    # compute new guesses according to the newton-raphson method until stopping criteria are met
    while eps_a > eps_s:
        xn = xk-f(xk, freq)/dfdx(xk, freq)
        d.append(xn)
        eps_a = np.abs((xn-xk)/xn)
        error.append(eps_a)
        niter += 1
        xk=xn
    
    return xk, niter, error