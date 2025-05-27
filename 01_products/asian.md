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

From a structuring desk perspective, Asian-style averaging often serves as the **embedded payoff mechanism** within broader structured products, including:
- **Accrual notes** (e.g., range accruals using daily or monthly averages)
- **Cliquet-style structures** with averaging resets over observation intervals
- **Step-down autocalls** or **defensive barrier notes** with coupons tied to average performance

---

## Payoff Mechanics

Asian options derive their value from averaging a set of underlying fixings, which directly impacts both their payoff shape and sensitivity profile. The two most common averaging approaches are:

- **Arithmetic averaging**, which takes the simple mean of observed prices
- **Geometric averaging**, which uses the nth root of the price product

The choice of averaging method can significantly affect option valuation and behavior:

- Arithmetic averages tend to be higher in upward-trending markets, making **arithmetic Asians more valuable** in bullish scenarios.
- Geometric averages are less volatile and always equal to or less than the arithmetic mean (by Jensen's inequality), making them useful for **analytic approximations** and **model calibration**.

While most real-world OTC products use **arithmetic averaging**, geometric variants are often studied in theory due to their mathematical tractability.

---

## Averaging Period & Fixing Conventions

The definition of the averaging period is just as important as the averaging method. Structurers must specify:

- **Start and end of the observation window:** Some notes average from trade date to maturity ("full averaging"), while others may only average in the last month ("partial averaging").
- **Fixing frequency:** Daily, weekly, or monthly. More frequent fixings produce smoother averages, but increase data handling and operational risk.
- **Fixing calendar:** Business day conventions apply. Holidays and market closures must be handled (e.g., next business day, modified following).
- **Lag structure:** Some notes use lagged fixings (e.g., T-1 or last business day of the previous month), which can affect hedge timing and client perception.
- **Forward-start averaging:** Especially common in structured notes, where averaging starts weeks or months after issuance.

These parameters have meaningful effects on:

- **Payoff shape** (e.g., a front-loaded average behaves differently than a back-loaded one)
- **Greek behavior** (e.g., Delta and Vega profiles over time)
- **Operational complexity** (fixing data feeds, fallback handling, etc.)

---

## Payoff Formulas

Asian options can be expressed under a generalized payoff structure:

$$
\text{Payoff} = \max\left( \phi \cdot (A - K), 0 \right)
$$

Where:

- $\phi=+1$ for a call, $\phi=-1$ for a put  
- $A$ is the average of the underlying (either arithmetic or geometric)  
- $K$ is the strike price

There are two main types of Asian options, depending on whether the **strike** or the **underlying** is averaged:

- **Average Price Option (APO)**, also called a **DPO** (Discounted Payoff Option):  
  The **underlying is averaged**, and payoff is compared to a fixed strike  
  → Most common in real-world structured products

- **Average Strike Option (ASO)**, also called a **DSO** (Discounted Strike Option):  
  The **strike is averaged**, and the final spot is used in payoff  
  → Rare in practice; more common in academic work or FX structuring

In structured notes and desk-level implementation, the DPO / Average Price format is by far the most widely used. The table below summarizes the typical payoff formulations under this approach:

---

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

While the previous sections covered the conceptual and structuring logic of Asian options, this section introduces how these payoffs are **programmatically represented and evaluated** in this repo.

Each product in `01_products/` exposes a consistent class interface, designed to be compatible with the pricing engines in `03_simulations/` and the stochastic models in `02_models/`.

At the core of every product class is:

- `payoff(path: List[float])`:  
  A **deterministic** function that returns the final payoff based on a given price path (i.e., once all fixings are known).
  
Optionally, classes may also include:

- `describe()`: Returns a product summary string
- `plot_payoff(path=None)`: Visualization support (for notebooks or diagnostics)

These conventions follow the design outlined in the repo's [README](../01_products/README.md).

### Implementation

```python
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
        # Optional: implement for diagnostics or Jupyter display
        pass
```

See implementation: [asian.py](../01_products/asian.py)

---

## Example Code Usage

```python
from products.asian import AsianOption

# Define an Asian call option
option = AsianOption(strike=100, option_type='call', average_type='arithmetic')

# Example fixing path (e.g., from GBM or historical)
path = [95, 98, 100, 102, 105]

# Compute deterministic payoff
print(option.payoff(path))      # Output: e.g., 2.0

# Print product description
print(option.describe())        # Output: "Arithmetic Asian call with strike 100"

# Optionally plot payoff along a simulated path
# option.plot_payoff(path)
