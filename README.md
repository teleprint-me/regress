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

This project provides a basic introduction to key concepts in statistics and regression analysis, such as the **mean**, **variance**, **covariance**, and **R-squared** value, all implemented using Python. The dataset used is hardcoded for simplicity, and the calculations are done manually to emphasize the underlying math.

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
Variance measures the spread of the dataset. It calculates how far each data point is from the mean and gives an idea of the data's distribution.

The variance ($\sigma^2$) is the average of these squared differences:

$$\text{Var}(x) = \sigma^2 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})^2}{n}$$

This gives a measure of how spread out the data is around the mean. A higher variance indicates more spread, while a lower variance indicates that the data is clustered more closely around the mean.

```python
def var(
    x: List[Union[int, float]], avg: Union[int, float], n: int
) -> float:
    """Calculates the variance of a list."""
    return sum((x_i - avg) ** 2 for x_i in x) / n
```

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
- [Statistics: The Easy Way](https://www.amazon.com/Statistics-Easy-Way/dp/0812093925)
