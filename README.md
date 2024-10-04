# Linear Regression

A simple implementation of linear regression from scratch using pure Python. This project walks through the fundamental concepts behind linear regression and demonstrates how to implement it without relying on third-party libraries.

## 1. Overview

This project provides a basic introduction to key concepts in statistics and regression analysis, such as the **mean**, **variance**, **covariance**, and **R-squared** value, all implemented using Python. The dataset used is hardcoded for simplicity, and the calculations are done manually to emphasize the underlying math.

## 2. Mean
The **mean** is the average of a dataset, which provides a central value around which the individual data points tend to cluster. In regression analysis, it helps establish a reference point to understand how the data is distributed.

### Mathematical Definition of Mean ($\mu$ or $\bar{x}$)

The mean of a dataset $x_1, x_2, \dots, x_n$ is given by the formula:

$$
\mu = \bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:
- $\mu$ and $\bar{x}$ represent the mean, or average, of the dataset.
- $x_i$ represents each data point in the dataset.
- $n$ is the number of data points — or observations.
- $\sum$ is the summation operator, meaning we sum all values of $x_i$.

This formula calculates the "average" value of the dataset by summing all the data points and dividing by the total number of observations.

### Why the Mean is Important in Regression
In the context of linear regression, the mean helps define the point through which the best-fit line passes. The best-fit line should pass through the point $(\bar{x}, \bar{y})$, where $\bar{x}$ is the mean of the independent variable and $\bar{y}$ is the mean of the dependent variable. This is why we often calculate the mean of both $x$ and $y$ when determining the slope and intercept of the regression line.

## 3. Variance
Variance measures the spread of the dataset. It calculates how far each data point is from the mean and gives an idea of the data's distribution.

## 4. Covariance
Covariance assesses how much two variables change together. Positive covariance indicates that the variables tend to move in the same direction, while negative covariance means they move in opposite directions.

## 5. Regression
Linear regression finds the line of best fit for a set of data points by minimizing the sum of squared errors. The line is represented by the equation:

$$y = mx + b$$

Where:
- $m$ is the slope
- $b$ is the intercept

## 6. Coefficient of Determination ($R^2$)
The $R^2$ value measures how well the regression line fits the data. It is calculated as:

$$ R^2 = 1 - \frac{SS_{residual}}{SS_{total}} $$

An $R^2$ value close to 1 indicates a strong fit.

## 7. Prediction
Once the regression line is calculated, it can be used to predict values of the dependent variable based on the independent variable.

## 8. How to Run

To run the project, simply clone the repository and execute the script:

```sh
git clone https://github.com/teleprint-me/regress.git
cd regress
python -m linear.regression
```

This will output:
- The slope ($m$) and intercept ($b$),
- Predicted values based on the regression line,
- The $R^2$ value to assess the accuracy of the model.

## 9. Resources

- [Mean](https://byjus.com/maths/mean/)
- [Variance](https://byjus.com/maths/variance/)
- [Covariance](https://byjus.com/maths/covariance/)
- [Regression](https://stats.libretexts.org/Courses/Las_Positas_College/Math_40%3A_Statistics_and_Probability/10%3A_Correlation_and_Regression/10.02%3A_The_Regression_Equation)
- [Prediction](https://stats.libretexts.org/Courses/Las_Positas_College/Math_40%3A_Statistics_and_Probability/10%3A_Correlation_and_Regression/10.02%3A_The_Regression_Equation/10.2.01%3A_Prediction)
