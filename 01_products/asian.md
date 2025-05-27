# Asian Options

Asian options are a class of **path-dependent exotic options** where the payoff is derived from the **average price** of the underlying asset over a specified observation period, rather than a single spot price at maturity.

Unlike European options, which are highly sensitive to terminal price levels, Asian options offer **smoothed exposure** over time. This structure is particularly useful for investors or issuers aiming to **reduce volatility risk**, **dampen manipulation risk**, or **engineer yield in a stable corridor**.

They are frequently used in:
- **Commodities**, where terminal spikes are common (e.g., energy, metals)
- **FX-linked notes**, especially dual-currency or quanto notes
- **Equity structured products** like range accruals or Phoenix autocalls with averaging features

---

## Structuring Motivation

- Reduce **spot price sensitivity** near maturity
- Mitigate **"fixing risk"** in thin or illiquid markets
- Offer more **stable exposure** for investment-linked insurance products
- Enable **coupon-linked exotic notes** based on average performance

From a **desk perspective**, Asian structures often form the **payoff layer** embedded in:
- Accrual notes
- Cliquet structures with averaging resets
- Step-down coupons or defensive barrier autocalls

---

## Key Variants

| Type             | Average Type | Payoff Formula                        |
|------------------|---------------|----------------------------------------|
| Call             | Arithmetic    | max(Avg(S) - K, 0)                     |
| Put              | Arithmetic    | max(K - Avg(S), 0)                     |
| Call             | Geometric     | max(Geomean(S) - K, 0)                 |
| Put              | Geometric     | max(K - Geomean(S), 0)                 |

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

