Title: Changepoint detection with Gaussian processes
Date: 2026-09-04
Category: Publications
Slug: publications
Author: Janneke Verbeek
Summary: Post about Offline changepoint detection with Gaussian processes
Status: published

In the paper *Offline changepoint detection with Gaussian processes* (2025, published at UAI), we applied Gaussian process regression to the problem of changepoint detection. The changepoint kernel, in combination with the spectral mixture kernel, turns out to be a really effective way to detect changepoints. 
The changepoint kernel (Lloyd, 2014) combines two base kernels, $k_1$ and $k_2$, with a sigmoid; the sigmoid is parametrized by a steepness $s$ and a location $x_0$, $\psi(x) = \frac{1}{(1-\exp(-s(x-x_0)}$, to smoothly transition between the functional forms described by the two base kernels. The full kernel is given by 
    $$k(x, x') = k_1(x, x')\cdot \bar\sigma + k_2(x, x') \cdot \sigma,$$
where $\psi(x, x') = \psi(x)\psi(x')$, $\bar \psi(x, x') = (1 - \psi(x)) (1 - \psi(x'))$. 

I intend to extend this post further with beautiful visualizations, but this was mostly a test to see how well the LaTeX renders and how a block of text looks. 



