# ADS Week 1, Time & Space Complexity

## Empirical Analysis
Empirical analysis is the process of running an algorithm with different input sizes and plotting/analyzin the change in input times overtime.

### Drawbacks of empirical analysis
- Runtime differs between different hardware, not just between different hardware but between different runs.
- Does not cover all inputs, thus the inputs not tested are not covered by the empirical analysis.
- An algorithm must be fully implemented in order to test it, but we only want to implement the fastest algorithm.

## 7 Important Functions
### Constant function
A very simple function in the form $f(n) = c$ where c is a constant. 

### The logarithm function
The logaritm function is $f(n) = log(n)$

### The linear function
The linear function is, as you might have guessed a function increasing at a set rate. They are in the form $f(n) = an +b$. This function has a higher order than the logarithmic, and the N-log(N) functions.

### The N-log(N) function
They are functions in the form $f(n) = n log(n)$. They have a higher order than *logarithmic* functions, but a smaller order than *linear* functions.

### The quadratic function
These are basically a subset of polynomial time functions and are written in the form $f(n) = an^2 + bn + c$. They have the lowest order between the polynomials, but its order is higher than all the previous functions.

### Polynomials
Polynomials are basically functions that don’t have any terms with a factor less than 0. A polynomial’s degree is the term with the highest power in it. The higher a polynomial’s degree is, the higher its order in the big-Oh notation.

### The exponential function
These little fuckers are the worst of all, they are very slow, can be represented using formulas in the form $f(n) = a^n$ where $a \in \mathbb{Q}$.  They have the highest order between all the functions, and the order increases as a increases.


![[Images/2809E595-B410-465A-B5E4-65486A4A3C40.jpeg]]

> This is a small detail but there are two important functions that will come in handy throughout this course, *ceil* $\lceil x \rceil$ and *floor* $\lfloor x \rfloor$. Ceil basically rolls the number x into the closest greater integer, and floor the other way around, so $\lceil 16.2 \rceil = 17$ and $\lfloor 16.2 \rfloor = 16$.


## Asymptotic Analysis

### Big-Oh Notation

#### The easy way
Basically, if you have a function that consists of different versions of the **7 important functions** the one with the highest order/the one that changes with the highest values have the highest precedence. So, for example, the function $f(n) = 2n + n^2 + 3nlog_2(n) + 2^n + 6$ has the Big-Oh $O(2^n)$ since exponential functions have the highest order. 


#### The big-boy mathematical way
