"""
Asian Options

Asian options are path-dependent options where the payoff depends on the average price of the underlying asset over a period of time. These are commonly used in commodities, FX, and equity derivatives markets to smooth volatility effects and reduce exposure to price manipulation.

This module supports:
- Arithmetic average options (most common in practice)
- Geometric average options (analytically tractable, useful for testing)
- Call and put styles

Payoff Formula (Arithmetic Call):
    max(Avg(S) - K, 0)

Where:
    - Avg(S) is the arithmetic or geometric average of the underlying price path
    - K is the strike price

Typical Use Cases:
- Investors seeking exposure to the average price over time rather than spot price at expiry
- Structuring products with less gamma risk than standard options
- Managing mean-reversion risk in commodities or FX

"""

import numpy as np

class AsianOption:
    def __init__(self, strike, average_type='arithmetic', option_type='call'):
        self.strike = strike
        self.average_type = average_type
        self.option_type = option_type

    def payoff(self, path):
        if self.average_type == 'arithmetic':
            avg_price = np.mean(path)
        elif self.average_type == 'geometric':
            avg_price = np.exp(np.mean(np.log(path)))
        else:
            raise ValueError("average_type must be 'arithmetic' or 'geometric'")

        if self.option_type == 'call':
            return max(avg_price - self.strike, 0)
        elif self.option_type == 'put':
            return max(self.strike - avg_price, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")

    def describe(self):
        return f"{self.average_type.capitalize()} Asian {self.option_type} option with strike {self.strike}"
