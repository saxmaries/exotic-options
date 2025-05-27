# Asian Options

Asian options are a class of **path-dependent exotic derivatives** where the **payoff depends on the average price** of the underlying asset over a specified observation period, rather than a single terminal fixing.

This averaging mechanism provides **smoothed market exposure** and makes the option less sensitive to short-term volatility or final-day price spikes, unlike European-style options that are fully exposed to the terminal spot. As a result, Asian options are often used to **dampen price volatility**, **reduce manipulation risk**, and **create more stable payoff profiles**.

Although they can be traded as **standalone exotics**, in practice, Asian options are **more frequently embedded** within structured products. The averaging logic is commonly used as a building block to shape risk-reward dynamics, stabilize coupon outcomes, or meet specific investment mandates.

---

## Common Use Cases

Asian-style structures are widely used in asset classes and products where smoothing is essential:
- **Commodities**, where sharp end-of-period spikes are common (e.g., energy, industrial metals)
- **FX-linked structured notes**, including quanto and dual-currency formats
- **Equity structured products**, such as Phoenix autocalls, range accruals, and yield notes featuring average-based conditions

---

## Structuring Motivation

Averaging features are typically incorporated to:
- Reduce **spot price sensitivity** near maturity
- Mitigate **fixing risk** in thin or illiquid markets
- Provide **stable exposure** for insurance-wrapped or retail-linked strategies
- Facilitate **coupon-linked exotic payoffs** based on average asset behavior

---

## Desk-Level Integration

From a structuring desk perspective, Asian payoffs often serve as the **embedded mechanism** within broader structured products, including:
- **Accrual notes** (e.g., range accruals using daily or monthly averages)

- **Cliquet-style structures** with averaging resets over observation intervals

- **Step-down autocalls** or **defensive barrier notes** with coupons tied to average performance

---

## Key Variants

| Option Type             | Average Type  | Payoff Formula                         |
|-------------------------|---------------|----------------------------------------|
| Call                    | Arithmetic    | max(Avg(S) - K, 0)                     |
| Put                     | Arithmetic    | max(K - Avg(S), 0)                     |
| Call                    | Geometric     | max(Geomean(S) - K, 0)                 |
| Put                     | Geometric     | max(K - Geomean(S), 0)                 |

Where:

-`Avg(S)` is the arithmetic mean:

$$
\text{Avg}(S) = \frac{1}{n} \sum_{i=1}^n S_i
$$

-`Geomean(S)` is the geometric mean:

$$
\text{Geomean}(S) = \left( \prod_{i=1}^n S_i \right)^{1/n}
$$

And:

$$
K = \text{Strike Price}
$$

---

## Geometric vs Arithmetic – Why It Matters

- **Arithmetic average** is more commonly used in real-world structuring. It aligns with observable fixings and tends to produce **higher average values**, especially in rising markets.
- **Geometric average** is less volatile, always less than or equal to the arithmetic mean (by Jensen's inequality), and often used in:
  - Benchmarking closed-form solutions
  - Equity indices where log-normal averaging assumptions apply

While geometric options are less common in OTC products, they are excellent **academic proxies** and stress-testing tools due to their analytical tractability.

---

## Volatility & Greek Implications

Asian options exhibit:

| **Greek** | **Behavior vs Vanilla** | **Implication** |
|-----------|--------------------------|------------------|
| **Delta** | Flatter near expiry due to averaging dampening directionality | Less sensitive to spot changes, especially close to maturity |
| **Gamma** | Lower, as averaging smooths the payoff | Lower convexity → fewer sudden jumps in Delta; smoother PnL |
| **Vega**  | Significantly lower due to reduced impact of implied vol | Less exposed to volatility changes → cheaper in high-vol regimes |
| **Theta** | Less negative for long positions; less positive for short positions | Time decay is more gradual; long positions erode slower, short positions earn less |
| **Rho**   | Lower, due to dampened sensitivity to forward price | Less affected by interest rate changes |

This makes them attractive for **yield-enhancing** structures when issuers want exposure to average directional moves **without overpaying for vol**.

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

