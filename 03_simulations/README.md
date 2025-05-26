# Simulations

This folder contains Monte Carlo simulation logic.

Features:
- Path generation using selected models
- Discretization schemes (Euler, Milstein)
- Variance reduction techniques (e.g., antithetic sampling)
- Reproducible random seed setup

Simulations call `products/` for payoff and `models/` for dynamics.
