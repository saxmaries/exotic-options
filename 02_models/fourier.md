# Fourier Methods for Option Pricing

---

## Overview

Fourier methods provide an efficient way to price European-style derivatives when the **characteristic function** of the asset's log-price is known. This is common in many realistic models beyond Black-Scholes, including **stochastic volatility** and **Lévy jump processes**.

By working in the **frequency domain**, Fourier pricing transforms the valuation problem into one of integrating or inverting characteristic functions — allowing **fast, model-flexible computation** across a range of strikes.

---

## Why Use Fourier Pricing?

Fourier pricing is especially valuable when:

- You want to **evaluate many strikes** at once (e.g., for calibration)
- The model is **non-Gaussian** and lacks a closed-form density
- Monte Carlo would be too slow or noisy for smooth payoffs
- You're pricing **structured products** with embedded European options (e.g., digital autocalls, range accruals, cliquets)

---

## Fourier Basics

A **characteristic function** of a random variable $X$ is defined as:

$$
\phi(u) = \mathbb{E}[e^{iuX}]
$$

For option pricing, we typically define $X = \ln S_T$, the log of the terminal asset price. Under the **risk-neutral measure**, this gives the CF of the log-price dynamics.

Key properties:
- Always exists (unlike density functions)
- Uniquely identifies the distribution
- Easier to compute in many models (e.g., Heston, VG)

---

## Carr-Madan Method (1999)

Carr & Madan proposed a widely used Fourier approach to price European calls using the characteristic function $\phi(u)$ of $\ln S_T$.

They introduced a **damping factor** $\alpha > 0$ to make the payoff integrable, and used the Fourier transform to price options across a strike grid.

### Core Formula

The price of a European call option is given by:

$$
C(K) = \frac{e^{-\alpha k}}{\pi} \int_0^\infty \Re \left[ e^{-iuk} \cdot \frac{\phi(u - i(\alpha + 1))}{\alpha^2 + \alpha - u^2 + i(2\alpha + 1)u} \right] \, du
$$

Where:
- $k = \ln K$, the log-strike
- $\phi(u)$ is the characteristic function of $\ln S_T$
- $\alpha$ is the damping parameter
- $\Re[\cdot]$ takes the real part

This integral can be computed efficiently using the **Fast Fourier Transform (FFT)**.

---

## In This Repo

The Fourier logic lives in:  
`02_models/fourier_pricing.py`

You can price a grid of call options using:

```python
from models.fourier_pricing import FourierPricer, bs_char_func

phi = lambda u: bs_char_func(u, S0=100, r=0.05, sigma=0.2, T=1.0)
pricer = FourierPricer(phi)
strikes = np.linspace(80, 120, 50)
prices = pricer.price_calls(S0=100, K_array=strikes, r=0.05, T=1.0)

