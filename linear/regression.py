"""
Copyright (C) 2024 Austin Berrio

Script: linear.regression

A simple example of linear regression in pure python completely from scratch.
"""

from typing import List, Union


def mean(vector: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the mean (average) of a list."""
    return sum(vector) / len(vector)


def variance(x: List[Union[int, float]], avg: Union[int, float]) -> float:
    """Calculates the variance of a list."""
    return sum((x_i - avg) ** 2 for x_i in x) / len(x)


def expectation(values: List[Union[int, float]], probabilities: List[float]) -> float:
    """Calculates the expectation of a random variable."""
    return sum(value * prob for value, prob in zip(values, probabilities))


def covariance(
    x: List[Union[int, float]],
    y: List[Union[int, float]],
    x_avg: float,
    y_avg: float,
) -> float:
    """Calculates the covariance of x and y."""
    return sum((x_i - x_avg) * (y_i - y_avg) for x_i, y_i in zip(x, y)) / len(x)


def linear_regression(x: List[Union[int, float]], y: List[Union[int, float]], n: int):
    """Calculates the slope (m) and intercept (b) for linear regression."""
    x_avg = mean(x)
    y_avg = mean(y)

    # Calculate x^2 and x*y for averages
    x_squared_avg = mean([x_i**2 for x_i in x])
    xy_avg = mean([x_i * y_i for x_i, y_i in zip(x, y)])

    # Calculate slope (m) and intercept (b)
    m_hat = (xy_avg - x_avg * y_avg) / (x_squared_avg - x_avg**2)
    b_hat = y_avg - m_hat * x_avg

    return m_hat, b_hat


def predict(x: List[Union[int, float]], m: float, b: float) -> List[float]:
    """Predicts values of y using the linear equation y = mx + b."""
    return [m * x_i + b for x_i in x]


def r_squared(
    y_actual: List[Union[int, float]], y_pred: List[float], y_avg: float, n: int
) -> float:
    """Calculates the coefficient of determination for the predictions."""
    ss_total = sum((y_i - y_avg) ** 2 for y_i in y_actual)  # Total sum of squares
    ss_residual = sum(
        (y_i - y_pred_i) ** 2 for y_i, y_pred_i in zip(y_actual, y_pred)
    )  # Residual sum of squares
    return 1 - (ss_residual / ss_total)


def main():
    # Pizza sales dataset
    income = [5, 10, 20, 8, 4, 6, 12, 15]
    sales = [27, 46, 73, 40, 30, 28, 46, 59]

    # Number of observations
    n = len(income)

    # Linear regression calculation
    m_hat, b_hat = linear_regression(income, sales, n)

    print(f"Slope (m): {m_hat}, Intercept (b): {b_hat}")

    # Predicted values
    predicted_sales = predict(income, m_hat, b_hat)
    print(f"Predicted sales: {predicted_sales}")

    # Calculate R-squared value
    y_avg = mean(sales)
    # Number of variations in y that can be explained by variations in x
    r2 = r_squared(sales, predicted_sales, y_avg, n)
    print(f"R-squared: {r2}")


if __name__ == "__main__":
    main()
