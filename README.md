# Linear Regression

A simple implementation of linear regression from scratch using pure Python. This project walks through the fundamental concepts behind linear regression and demonstrates how to implement it without relying on third-party libraries.

## Overview

This project provides a basic introduction to key concepts in statistics and regression analysis, such as the **mean**, **variance**, **covariance**, and **R-squared** value, all implemented using Python. The dataset used is hardcoded for simplicity, and the calculations are done manually to emphasize the underlying math.

## Sections

### 1. Mean
The mean is the average of the dataset, which provides a central value to compare individual data points.

### 2. Variance
Variance measures the spread of the dataset. It calculates how far each data point is from the mean and gives an idea of the data's distribution.

### 3. Covariance
Covariance assesses how much two variables change together. Positive covariance indicates that the variables tend to move in the same direction, while negative covariance means they move in opposite directions.

### 4. Regression
Linear regression finds the line of best fit for a set of data points by minimizing the sum of squared errors. The line is represented by the equation:

$$y = mx + b$$

Where:
- $m$ is the slope
- $b$ is the intercept

### 5. Coefficient of Determination ($R^2$)
The $R^2$ value measures how well the regression line fits the data. It is calculated as:

$$ R^2 = 1 - \frac{SS_{residual}}{SS_{total}} $$

An $R^2$ value close to 1 indicates a strong fit.

### 6. Prediction
Once the regression line is calculated, it can be used to predict values of the dependent variable based on the independent variable.

## How to Run

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

## Resources

- [Mean](https://byjus.com/maths/mean/)
- [Variance](https://byjus.com/maths/variance/)
- [Covariance](https://byjus.com/maths/covariance/)
- [Regression](https://stats.libretexts.org/Courses/Las_Positas_College/Math_40%3A_Statistics_and_Probability/10%3A_Correlation_and_Regression/10.02%3A_The_Regression_Equation)
- [Prediction](https://stats.libretexts.org/Courses/Las_Positas_College/Math_40%3A_Statistics_and_Probability/10%3A_Correlation_and_Regression/10.02%3A_The_Regression_Equation/10.2.01%3A_Prediction)
