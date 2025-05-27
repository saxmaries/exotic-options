# Asian Options

Asian options are a class of **path-dependent exotic options** where the payoff is based on the **average price** of the underlying asset over a period, rather than its price at maturity.

They are widely used in **FX**, **commodities**, and **equities** to:
- Smooth out price spikes
- Reduce market manipulation risk
- Reduce volatility exposure

---

## Key Variants

| Type             | Average Type | Payoff Formula                        |
|------------------|---------------|----------------------------------------|
| Arithmetic Call  | Arithmetic    | max(Avg(S) - K, 0)                     |
| Arithmetic Put   | Arithmetic    | max(K - Avg(S), 0)                     |
| Geometric Call   | Geometric     | max(Geomean(S) - K, 0)                 |
| Geometric Put    | Geometric     | max(K - Geomean(S), 0)                 |

Where:
- `Avg(S)` is the arithmetic mean: \(\frac{1}{n} \sum_{i=1}^n S_i\)
- `Geomean(S)` is the geometric mean: \((\prod_{i=1}^n S_i)^{1/n}\)
- `K` is the strike price

---

## Class Interface

Each Asian option implements the following methods:

- `payoff(path: List[float]) -> float`  
  Returns the deterministic payoff based on a given price path.

- `describe() -> str`  
  Returns a human-readable product description.

- `plot_payoff(path=None)`  
  (Optional) Visualizes payoff behavior along a price path.

These are designed to be **used by pricing engines in `03_simulations/`**.

---

## Example Code Usage

```python
from products.asian import AsianOption

# Define an Asian arithmetic call
option = AsianOption(strike=100, average_type='arithmetic', option_type='call')

# Simulated path (e.g., from GBM or real market data)
path = [95, 98, 100, 102, 105]

# Compute deterministic payoff
print(option.payoff(path))  # e.g., returns 2.0

# Optional: get product description
print(option.describe())    # e.g., "Arithmetic Asian call with strike 100"


$$
\left( \prod_{i=1}^{n} S_i \right)^{1/n}
$$
