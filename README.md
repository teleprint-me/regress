# Linear Regression

A simple implementation of linear regression from scratch using pure Python. This project walks through the fundamental concepts behind linear regression and demonstrates how to implement it without relying on third-party libraries.

## Table of Contents
1. Overview
2. Mean
3. Variance
4. Event
5. Probability
6. Expectation
7. Covariance
8. Regression
9. Determination
10. Prediction
11. How to Run
12. Resources

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

## 4. Event

An **event** is a specific outcome or a set of outcomes from a sample space. In probability theory, events are subsets of the sample space, which contains all possible outcomes of a random experiment. Understanding events is essential to calculating probabilities and analyzing data.

### Sample Space and Events

The **sample space** (denoted $S$) is the set of all possible outcomes in a given experiment. An **event** is any subset of this sample space. For example, when rolling a six-sided die, the sample space is:

$$S = \{1, 2, 3, 4, 5, 6\}$$

Each outcome in this sample space (i.e., rolling a specific number) is considered an **element** of the sample space and can be treated as an event:

$$s \in S$$

The **cardinality** of the sample space, or the number of possible outcomes, is represented by $|S|$. For a six-sided die, the cardinality is:

$$|S| = 6$$

### Example of an Event

Suppose we are interested in the event of rolling a 3. In this case, the event $A$ is defined as:

$$A = \{3\}$$

This is a subset of the sample space, containing just one element (rolling a 3). The number of ways this event can occur is $N(A) = 1$, since there is exactly one way to roll a 3.

### Probability of an Event

The probability of an event is calculated by dividing the number of favorable outcomes by the total number of possible outcomes in the sample space:

$$Pr(A) = \frac{N(A)}{N(S)}$$

Where:
- $N(A)$ is the number of favorable outcomes (the number of ways the event $A$ can occur),
- $N(S)$ is the total number of possible outcomes in the sample space.

For example, the probability of rolling a 3 on a six-sided die is:

$$Pr(3) = \frac{1}{6}$$

This is because there is 1 favorable outcome (rolling a 3) out of 6 possible outcomes in total.

### Python Code for Calculating Event Probability

Here’s a simple function to calculate the probability of an event in a sample space:

```python
def event_probability(favorable_outcomes: int, total_outcomes: int) -> float:
    """Calculates the probability of an event."""
    return favorable_outcomes / total_outcomes
```

#### Example:

Using this function, you can calculate the probability of rolling a 3 on a six-sided die:

```python
favorable = 1  # Rolling a 3
total = 6      # Six sides of the die
probability_of_3 = event_probability(favorable, total)
print(f"Probability of rolling a 3: {probability_of_3}")
```

This will calculate and print the probability of rolling a 3, which is $\frac{1}{6}$.

### Conclusion

An **event** is a subset of the sample space, representing one or more possible outcomes of a random experiment. Understanding events and their probabilities is a key building block in probability theory, which helps in analyzing real-world data and random processes.

## 5. Probability

**Probability** is the measure of the likelihood that an event will occur. It quantifies the uncertainty of different outcomes in an experiment or random process. The probability of an event is a number between 0 and 1, where:
- 0 means the event will not occur, and 
- 1 means the event will definitely occur.

### Mathematical Definition of Probability

The probability of an event $A$, denoted $Pr(A)$, is defined as:

$$Pr(A) = \frac{N(A)}{N(S)}$$

Where:
- $N(A)$ is the number of favorable outcomes (the number of ways event $A$ can occur),
- $N(S)$ is the total number of possible outcomes in the sample space $S$.

For example, when flipping a fair coin:
- The probability of getting heads is $Pr(\text{Heads}) = \frac{1}{2}$, since there is 1 favorable outcome (heads) out of 2 possible outcomes (heads or tails).

### Intuition Behind Probability

Probability helps quantify uncertainty. It tells us how likely a certain event is, based on the number of ways it can happen compared to all possible outcomes. In linear regression, probability forms the foundation for understanding more complex concepts like **expectation** and **covariance**, especially when analyzing data that involves random variables.

### Types of Probability
- **Theoretical Probability**: Based on reasoning (e.g., the probability of rolling a 3 on a fair 6-sided die is $\frac{1}{6}$).
- **Empirical Probability**: Based on observations or experiments (e.g., estimating the probability of rain by observing past weather patterns).

### Python Code for Calculating Probability

Here’s a basic function to calculate the probability of an event:

```python
def probability(favorable_outcomes: int, total_outcomes: int) -> float:
    """Calculates the probability of an event."""
    return favorable_outcomes / total_outcomes
```

#### Explanation:
- **Input**:
  - `favorable_outcomes`: The number of ways the event can occur.
  - `total_outcomes`: The total number of possible outcomes in the sample space.
- **Output**: The probability of the event.
- **Efficiency**: A simple division provides the probability.

#### Example:

```python
favorable = 1  # Getting heads
total = 2      # Heads or tails
coin_flip_probability = probability(favorable, total)
print(f"Probability of getting heads: {coin_flip_probability}")
```

This will calculate the probability of getting heads when flipping a fair coin.

### Conclusion

**Probability** serves as the foundation for many concepts in statistics and regression analysis, including expectation and covariance. Understanding how likely certain outcomes are allows us to model and predict real-world events with more confidence.

## 6. Expectation

**Expectation** (also known as the **expected value** or **mean** in some contexts) is a fundamental concept in probability and statistics. It represents the average or mean value of a random variable, weighted by the probabilities of the different outcomes. Expectation helps us summarize the central tendency of a random variable's probability distribution.

### Mathematical Definition of Expectation ($E(X)$)

The expectation ($\mathbb{E}$) of a discrete random variable $X$ is calculated by summing all possible values of $X$, each weighted by its corresponding probability:

$$E(X) = \sum_{i=1}^{n} p_i \cdot x_i$$

Where:
- $x_i$ is a possible value that the random variable $X$ can take.
- $p_i$ is the probability that $X$ takes the value $x_i$.
- $\sum$ indicates the summation of all possible outcomes.

### Intuition Behind Expectation

Expectation can be thought of as the "long-run average" of a random variable if the process that generates it is repeated many times. For example, if we repeatedly toss a weighted coin, the expectation helps us understand what the average result would be over time, based on the probabilities of heads and tails.

In the context of linear regression, the expectation gives us a way to handle variables that vary randomly, helping us define relationships like covariance between two random variables.

### Python Code for Calculating Expectation

Here’s how you might implement the expectation for a discrete set of values:

```python
def expectation(values: List[Union[int, float]], probabilities: List[float]) -> float:
    """Calculates the expectation of a random variable."""
    return sum(value * prob for value, prob in zip(values, probabilities))
```

#### Explanation:
- **Input**:
  - `values`: A list of possible outcomes (e.g., values the random variable can take).
  - `probabilities`: A list of corresponding probabilities for each outcome.
- **Output**: The expected value of the random variable.
- **Efficiency**: Uses `zip` to pair values with their probabilities and compute the weighted sum.

#### Example:

```python
outcomes = [1, 2, 3, 4, 5]
probabilities = [0.1, 0.2, 0.3, 0.2, 0.2]

expected_value = expectation(outcomes, probabilities)
print(f"Expected value: {expected_value}")
```

This will calculate the expectation based on the outcomes and their probabilities, giving you an understanding of the average result.

### Conclusion

The **expectation** is essential for understanding many statistical concepts, including covariance, which measures how two variables change together. It is often used in regression analysis to summarize how data is distributed and to explore relationships between variables.

## 7. Covariance

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

### Conclusion:

Covariance helps quantify the relationship between two variables in terms of their directional movement. In linear regression, it plays a vital role in understanding how the independent and dependent variables are related, ultimately influencing the calculation of the slope in the regression equation.

## 8. Regression

Linear regression is a method used to find the line of best fit for a set of data points by minimizing the sum of squared errors (SSE). The goal is to find the equation of a line that best represents the relationship between an independent variable $x$ and a dependent variable $y$.

### Equation of the Line

The equation for a simple linear regression line is given by:

$$
y = \hat{m} \cdot x + \hat{b}
$$

Where:
- $\hat{m}$ is the **slope** of the line, representing how much $y$ changes for each unit change in $x$.
- $\hat{b}$ is the **intercept**, representing the value of $y$ when $x = 0$.

### Calculating the Slope and Intercept

The slope $\hat{m}$ and intercept $\hat{b}$ can be calculated using the following formulas:

$$
\hat{m} = \frac{\bar{xy} - \bar{x} \cdot \bar{y}}{\bar{x^2} - \bar{x}^2}
$$
$$
\hat{b} = \bar{y} - \hat{m} \cdot \bar{x}
$$

Where:
- $\bar{x}$ is the mean of the $x$-values.
- $\bar{y}$ is the mean of the $y$-values.
- $\bar{xy}$ is the mean of the products $x_i \cdot y_i$.
- $\bar{x^2}$ is the mean of the squares of the $x$-values.

These formulas allow us to calculate the best-fit line using the means of the data.

### Error (Residual)

The **error** or **residual** for each data point $(x_i, y_i)$ is the difference between the observed $y_i$ and the predicted value $\hat{y}_{x_i}$ from the regression line:

$$
\text{error}_i = y_i - \hat{y}_{x_i}
$$

Where $\hat{y}_{x_i}$ is the predicted value given by:

$$
\hat{y}_{x_i} = \hat{m} \cdot x_i + \hat{b}
$$

### Minimizing the Sum of Squared Errors

The line of best fit is found by minimizing the sum of squared errors (SSE), which is the sum of the squared differences between the observed and predicted values:

$$
SSE = \sum_{i=1}^{n} [y_i - (\hat{m} \cdot x_i + \hat{b})]^2
$$

This ensures that the regression line is the best possible fit for the given data points by reducing the overall error.

## 9. Coefficient of Determination ($r^2$)
The $r^2$ value measures how well the regression line fits the data. It is calculated as:

$$ r^2 = 1 - \frac{SE_{residual}}{SE_{total}} $$

An $r^2$ value close to 1 indicates a strong fit.

## 10. Prediction
Once the regression line is calculated, it can be used to predict values of the dependent variable based on the independent variable.

## 11. How to Run

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

## 12. Resources

- [Mean](https://byjus.com/maths/mean/)
- [Variance](https://byjus.com/maths/variance/)
- [Covariance](https://byjus.com/maths/covariance/)
- [Regression](https://stats.libretexts.org/Courses/Las_Positas_College/Math_40%3A_Statistics_and_Probability/10%3A_Correlation_and_Regression/10.02%3A_The_Regression_Equation)
- [Prediction](https://stats.libretexts.org/Courses/Las_Positas_College/Math_40%3A_Statistics_and_Probability/10%3A_Correlation_and_Regression/10.02%3A_The_Regression_Equation/10.2.01%3A_Prediction)
- [Statistics: The Easy Way](https://www.amazon.com/Statistics-Easy-Way/dp/0812093925)
