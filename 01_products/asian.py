"""
Asian Options

This module defines the payoff structure for Asian options — exotic derivatives whose payoffs depend on the average price of the underlying asset over a time period.

Variants supported:
- Arithmetic average (most commonly used in the market)
- Geometric average (used for analytical testing or benchmarking)
- Call and Put styles

Payoff formulas:
- Arithmetic Call:  max(Avg(S) - K, 0)
- Arithmetic Put:   max(K - Avg(S), 0)
- Geometric Call:   max(Geomean(S) - K, 0)
- Geometric Put:    max(K - Geomean(S), 0)

Where:
    - Avg(S) = (1/n) * sum of prices
    - Geomean(S) = (∏ Sᵢ)^(1/n)
    - K is the strike price

This file does not perform any path simulation. For that, use models in `02_models/` and pricers in `03_simulations/`.
"""

import numpy as np
import matplotlib.pyplot as plt


class AsianOption:
    def __init__(self, strike, average_type='arithmetic', option_type='call'):
        """
        Initializes an Asian option.

        Parameters:
        - strike (float): Strike price
        - average_type (str): 'arithmetic' or 'geometric'
        - option_type (str): 'call' or 'put'
        """
        self.strike = strike
        self.average_type = average_type.lower()
        self.option_type = option_type.lower()

        if self.average_type not in ['arithmetic', 'geometric']:
            raise ValueError("average_type must be 'arithmetic' or 'geometric'")
        if self.option_type not in ['call', 'put']:
            raise ValueError("option_type must be 'call' or 'put'")

    def payoff(self, path):
        """
        Computes the deterministic payoff of the Asian option given a price path.

        Parameters:
        - path (List[float]): Simulated or historical underlying price path

        Returns:
        - float: Option payoff
        """
        if not isinstance(path, (list, np.ndarray)) or len(path) == 0:
            raise ValueError("Input path must be a non-empty list or array of prices.")

        if self.average_type == 'arithmetic':
            avg_price = np.mean(path)
        else:  # geometric
            avg_price = np.exp(np.mean(np.log(path)))

        if self.option_type == 'call':
            return max(avg_price - self.strike, 0)
        else:  # put
            return max(self.strike - avg_price, 0)

    def describe(self):
        """
        Returns a human-readable string describing the product.
        """
        return f"{self.average_type.capitalize()} Asian {self.option_type} option with strike {self.strike}"

    def plot_payoff(self, path=None):
        """
        Plots a visual payoff profile using either a single input path or synthetic sweep.

        Parameters:
        - path (List[float], optional): If provided, shows payoff for that path.
                                        Otherwise, sweeps hypothetical average prices.
        """
        if path is not None:
            payoff = self.payoff(path)
            label = f"Payoff for sample path (avg={np.mean(path):.2f})"
            avg_prices = [np.mean(path)]
            payoffs = [payoff]
        else:
            avg_prices = np.linspace(0.5 * self.strike, 1.5 * self.strike, 100)
            if self.option_type == 'call':
                payoffs = np.maximum(avg_prices - self.strike, 0)
            else:
                payoffs = np.maximum(self.strike - avg_prices, 0)
            label = f"{self.option_type.capitalize()} payoff vs. average price"

        plt.figure(figsize=(6, 4))
        plt.plot(avg_prices, payoffs, label=label)
        plt.axvline(self.strike, linestyle='--', color='gray', label='Strike')
        plt.title(f"{self.describe()} – Payoff")
        plt.xlabel("Average Price")
        plt.ylabel("Payoff")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.show()

