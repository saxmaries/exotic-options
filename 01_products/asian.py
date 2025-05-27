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
"""

from typing import List
from .base_product import BaseProduct  # adjust import if needed

class AsianOption(BaseProduct):
    def __init__(self, strike: float, option_type: str = "call", average_type: str = "arithmetic"):
        self.strike = strike
        self.option_type = option_type
        self.average_type = average_type

    def payoff(self, path: List[float]) -> float:
        if self.average_type == "arithmetic":
            avg = sum(path) / len(path)
        elif self.average_type == "geometric":
            product = 1
            for p in path:
                product *= p
            avg = product ** (1 / len(path))
        else:
            raise ValueError("Unsupported average type")

        intrinsic = avg - self.strike if self.option_type == "call" else self.strike - avg
        return max(intrinsic, 0)

    def describe(self) -> str:
        return f"{self.average_type.capitalize()} Asian {self.option_type} with strike {self.strike}"

    def plot_payoff(self, path=None):
        # Optional: implement for Jupyter usage or diagnostics
        pass
