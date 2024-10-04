# Linear Regression

A simple implementation of linear regression from scratch using pure Python. This project walks through the fundamental concepts behind linear regression and demonstrates how to implement it without relying on third-party libraries.

## Table of Contents
1. Overview
2. Mean
3. Variance
4. Covariance
5. Regression
6. Coefficient of Determination
7. Prediction
8. How to Run
9. Resources

## 1. Overview

This project provides a basic introduction to key concepts in statistics and regression analysis, such as the **mean**, **variance**, **covariance**, and **r-squared** value, all implemented using Python. The dataset used is hardcoded for simplicity, and the calculations are done manually to emphasize the underlying math.

### Dataset

The dataset consists of observations of average income and total pizza sales for a 1-month period across eight different towns:

| Town | Income (thousands of dollars) | Pizza Sales (in thousands) |
| ---  | ---                           | ---                        |
| 1    | 5                             | 27                         |
| 2    | 10                            | 46                         |
| 3    | 20                            | 73                         |
| 4    | 8                             | 40                         |
| 5    | 4                             | 30                         |
| 6    | 6                             | 28                         |
| 7    | 12                            | 46                         |
| 8    | 15                            | 59                         |

The **income** represents the independent variable (input), and the **pizza sales** represent the dependent variable (output) that we aim to predict using linear regression.

## 2. Mean

The **mean** is the central value of a dataset, often referred to as the "average." In regression analysis, the mean helps provide a reference point for understanding how the data is distributed, which plays a critical role in determining the best-fit line for the data.

### Mathematical Definition of the Mean ($\mu$ or $\bar{x}$)

The mean of a dataset $x_1, x_2, \dots, x_n$ is given by the formula:

$$
\mu = \bar{x} = \frac{x_1 + x_2 + \dots + x_n}{n} = \frac{\sum_{i=1}^{n} x_i}{n}
$$

Where:
- $\mu$ or $\bar{x}$ represents the mean (average) of the dataset.
- $x_i$ is an individual data point in the dataset.
- $n$ is the number of data points (observations).
- $\sum$ is the summation symbol, indicating that we sum all values of $x_i$.

This formula calculates the mean by summing all data points and dividing by the total number of observations. The mean helps establish the **central tendency** of the data—how the data points are distributed around a central value.

### Intuition Behind the Mean

The mean provides a single value that summarizes the entire dataset. It is particularly useful in linear regression because the best-fit line (regression line) always passes through the point $(\bar{x}, \bar{y})$, where $\bar{x}$ is the mean of the independent variable $x$ and $\bar{y}$ is the mean of the dependent variable $y$.

By calculating the mean of both $x$ and $y$, we can anchor the regression line to this point, ensuring that the line represents the data’s central tendency.

### Python Code for Calculating the Mean

The mean calculation in Python directly follows the mathematical formula:

```python
def mean(vector: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the mean (average) of a list."""
    return sum(vector) / len(vector)
```

#### Explanation
- **Input**: A list of numerical values (either integers or floats).
- **Output**: The mean of the list, calculated by summing all elements and dividing by the number of elements.
- **Efficiency**: The number of observations $n$ is calculated within the function using `len(vector)`, so it does not need to be passed separately.

#### Example

Given the dataset of incomes:

```python
income = [5, 10, 20, 8, 4, 6, 12, 15]
```

We can calculate the mean of the incomes as:

```python
income_mean = mean(income)
print(f"Mean of incomes: {income_mean}")
```

This will output the average income for the dataset, which is the central value around which all other values tend to cluster.

### Conclusion

The **mean** is foundational in both statistics and regression analysis. In regression, it helps to establish the position of the best-fit line, ensuring that the line reflects the central tendency of the data.

## 3. Variance
Variance measures the spread of the dataset. It quantifies how much the individual data points deviate from the mean, providing a sense of how "spread out" or "close together" the data points are.

### Mathematical Definition of Variance ($\sigma^2$)

The variance of a dataset $x_1, x_2, \dots, x_n$ is given by:

$$
\text{Var}(x) = \sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}
$$

Where:
- $x_i$ is an individual data point in the dataset.
- $\bar{x}$ is the mean of the dataset.
- $n$ is the number of data points.
- $\sum$ represents the summation over all the data points.

This formula calculates the variance by summing the squared differences between each data point and the mean, and then dividing by the number of data points. A higher variance indicates that the data points are more spread out, while a lower variance means that the data is clustered more closely around the mean.

### Python Implementation

To compute the variance, we implement the following function:

```python
def variance(x: List[Union[int, float]], avg: Union[int, float]) -> float:
    """Calculates the variance of a list."""
    return sum((x_i - avg) ** 2 for x_i in x) / len(x)
```

#### Explanation
- **Input**: 
  - `x`: A list of numerical values (either integers or floats).
  - `avg`: The mean of the list, which should be precomputed.
- **Output**: The variance of the dataset, which indicates how far the values deviate from the mean.
- **Efficiency**: The function automatically calculates the number of data points $n$ using `len(x)`, simplifying the input.

#### Example
Given the same dataset of incomes:

```python
income = [5, 10, 20, 8, 4, 6, 12, 15]
income_mean = mean(income)
income_variance = variance(income, income_mean)
print(f"Variance of incomes: {income_variance}")
```

This will output the variance of the incomes, providing insight into how spread out the income values are relative to the mean.

### Conclusion

Variance is a critical measure in regression analysis because it helps determine the spread of the data. In linear regression, understanding the variance of both the independent and dependent variables helps in modeling the relationship between them.

## 4. Covariance

Covariance measures how much two variables change together. It indicates the direction of the linear relationship between two variables. If the covariance is positive, it means that as one variable increases, the other tends to increase as well (and vice versa). A negative covariance indicates that as one variable increases, the other tends to decrease.

### Mathematical Definition of Covariance

The covariance between two variables $X$ and $Y$ is given by:

$$\text{Cov}(X, Y) = E[(X - E(X))(Y - E(Y))]$$

Where:
- $E(X)$ is the expected value (mean) of $X$,
- $E(Y)$ is the expected value (mean) of $Y$,
- $E(XY)$ is the expected value of the product $X \cdot Y$.

Using the distributive property and combining terms, we can simplify the formula to:

$$\text{Cov}(X, Y) = E(XY) - E(X) \cdot E(Y)$$

Where:
- $E(XY)$ represents the mean of the product of $X$ and $Y$,
- $E(X) \cdot E(Y)$ is the product of the means of $X$ and $Y$.

### Interpreting Covariance
- **Positive Covariance**: $X$ and $Y$ move in the same direction. When one increases, so does the other.
- **Negative Covariance**: $X$ and $Y$ move in opposite directions. When one increases, the other decreases.

Covariance is an important metric in regression analysis, as it helps in understanding how the independent variable $X$ and dependent variable $Y$ are related.

### Python Implementation

To compute the covariance between two datasets $x$ and $y$, we use the following function:

```python
def covariance(
    x: List[Union[int, float]],
    y: List[Union[int, float]],
    x_avg: float,
    y_avg: float,
) -> float:
    """Calculates the covariance of x and y."""
    return sum((x_i - x_avg) * (y_i - y_avg) for x_i, y_i in zip(x, y)) / len(x)
```

#### Explanation
- **Input**: 
  - `x`: A list of numerical values for the first variable (e.g., income).
  - `y`: A list of numerical values for the second variable (e.g., pizza sales).
  - `x_avg`: The mean of the list `x`.
  - `y_avg`: The mean of the list `y`.
- **Output**: The covariance between `x` and `y`.
- **Efficiency**: The function uses `zip(x, y)` to iterate through both lists simultaneously, calculating the covariance as the average of the product of their deviations from their means.

#### Example

Given the datasets for income and pizza sales:

```python
income = [5, 10, 20, 8, 4, 6, 12, 15]
sales = [27, 46, 73, 40, 30, 28, 46, 59]

income_mean = mean(income)
sales_mean = mean(sales)

income_sales_cov = covariance(income, sales, income_mean, sales_mean)
print(f"Covariance of income and sales: {income_sales_cov}")
```

This will output the covariance between the two datasets, indicating the direction of the relationship between income and pizza sales.

## 5. Regression
Linear regression finds the line of best fit for a set of data points by minimizing the sum of squared errors. The line is represented by the equation:

$$y = mx + b$$

Where:
- $m$ is the slope
- $b$ is the intercept

## 6. Coefficient of Determination ($r^2$)
The $r^2$ value measures how well the regression line fits the data. It is calculated as:

$$ r^2 = 1 - \frac{SE_{residual}}{SE_{total}} $$

An $r^2$ value close to 1 indicates a strong fit.

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
- [Statistics: The Easy Way](https://www.amazon.com/Statistics-Easy-Way/dp/0812093925)
