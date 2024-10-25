---
title:  Two Class Quadratic Classifier
date: 2024-10-22T12:39:04+02:00
description: 
tags: ["cs/ml"]
aliases: ['Two Class Quadratic Classifier']
---

It is a good exercise to analyze how to [[Using Bayes Rule|use the Bayes Rule]] to estimate the posterior probability for each class in a two class scenario.

The decision boundary can be identified as:

$$
f(\mathbf{x}) = \log \frac{p(y_1|\mathbf{x})}{p(y_2|\mathbf{x})} = \log 1
$$
$$
f(\mathbf{x}) = \log (y_1|\mathbf{x}) - \log p(y_2|\mathbf{x}) = 0
$$

Replacing the class conditional probabilities with the [[Gaussian Distribution|Gaussian Distribution]], we can derive that:

$$
p(y|\mathbf{x}) = \frac{p(\mathbf{x}|y)p(y)}{p(\mathbf{x})}
$$
$$
p(\mathbf{x}|y) = \frac{1}{(\sqrt{2\pi)^p det(\Sigma_y)}}exp(-\frac{1}{2}(x-\mu_y)\Sigma_y^{-1}(x-\mu_y))
$$

Deriving the logarithm of the class posteriors:

$$
\log(p(y|\mathbf{x}) = \frac{-p}{2}2\pi  - \frac{1}{2}det(\Sigma_y) -\frac{1}{2}(x-\mu_y)\Sigma_y^{-1}(x-\mu_y) + \log p(y) - \log p(\mathbf{x})
$$

Since $p(\mathbf{x})$ is independent of the class, it can be dropped, leaving us with:

$$
g_i(\mathbf{x}) = \frac{-p}{2}2\pi  - \frac{1}{2}det(\Sigma_{y_i}) -\frac{1}{2}(x-\mu_{y_i})\Sigma_{y_i}^{-1}(x-\mu_{y_i}) + \log p(y_i)
$$

Therefore, the classifier becomes $g_i(\mathbf{x}) > g_j(\mathbf{x})$. And the decision boundary becomes $f(\mathbf{x}) = g_2(\mathbf{x}) - g_1(\mathbf{x}) = 0$.

The function $f(\mathbf{x})$ can be written in the general form:

$$
f(\mathbf{x}) = \mathbf{x}^T\mathbf{W}\mathbf{x} + \mathbf{w}^T\mathbf{x} + w_0
$$
 where 

$$
\mathbf{W} = \frac{1}{2}(\Sigma_{2}^{-1} - \Sigma_{1}^{-1})
$$
$$
\mathbf{W} = \mu_1^T\Sigma_{1}^{-1} - \mu_2^T\Sigma_{2}^{-1}
$$

$$
w_0 = - \frac{1}{2} \log \det \Sigma_1 - \frac{1}{2} \mu_1^T \Sigma_1^{-1} \mu_1 + \log p(y_1) + \frac{1}{2} \log \det \Sigma_2 + \frac{1}{2} \mu_2^T \Sigma_2^{-1} \mu_2 - \log p(y_2)
$$

This leaves us with a quadratic decision boundary:

![[Pasted image 20241022132324.png]]

## What if the covariance matrix is non invertible?

In the case that one of the variances of a feature's variance is 0: we can not create an [[Inverse Matrix]] for $\Sigma$. So, instead we estimate a single covariance matrix for the entire dataset by averaging over the covariance matrices for all classes:

$$
\hat{\Sigma} = \frac{1}{N} \Sigma_{i=1}^N \Sigma_i
$$

Since we share a single covariance matrix across all classes, the matrix $\mathbf{W}$ becomes 0, turning $f(\mathbf{x}) = \mathbf{w}^T\mathbf{x} + w_0$, and making our decision boundary linear.

## No covariance matrix 🥺

If you are unable to even estimate a single covariance matrix, one can simply assume that the variance of each feature is the same and are independent from each other. This results in a covariance matrix in the form of: $\hat{\Sigma} = \sigma^2I$
