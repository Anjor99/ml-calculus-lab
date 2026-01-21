def numerical_derivative(f, x, h=1e-5):
    """
    Calculate the numerical derivative of a function f at point x using the central difference method.

    Parameters:
    f : function
        The function for which to calculate the derivative.
    x : float
        The point at which to calculate the derivative.
    h : float, optional
        A small step size for the finite difference approximation (default is 1e-5).

    Returns:
    float
        The numerical derivative of f at point x.
    """
    return (f(x + h) - f(x - h)) / (2 * h)