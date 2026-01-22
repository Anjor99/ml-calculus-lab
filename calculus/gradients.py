def gradient_descent_1d(
    f,
    df,
    x0,
    learning_rate=0.01,
    tolerance=1e-6,
    max_iterations=1000
):
    """
    Perform gradient descent on a 1D function.

    Returns:
    x_min : float
        Estimated minimizer.
    f_min : float
        Function value at the minimizer.
    history : list
        Values of x at each iteration (useful for plotting).
    """
    x = x0
    history = [x]

    for _ in range(max_iterations):
        grad = df(x)
        x_new = x - learning_rate * grad

        # convergence check
        if abs(x_new - x) < tolerance:
            break

        # divergence guard (learning-rate too large)
        if abs(x_new) > 1e6:
            raise ValueError("Gradient descent diverged. Try a smaller learning rate.")

        x = x_new
        history.append(x)

    return x, f(x), history
