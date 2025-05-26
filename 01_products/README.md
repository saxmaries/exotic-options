# Products

This folder defines exotic option payoff structures.

Each file implements a specific product type, such as:

- **Barrier options** (knock-in, knock-out)
- **Asian options** (arithmetic / geometric)
- **Digital / binary options**
- **Autocallables** (vanilla, Phoenix, worst-of)
- **Cliquet and path-dependent instruments**
- **Lookback options**
- **Range accruals**
- **Snowballs**
- **FX dual-currency structures**

Each product exposes a `payoff(path)` method, which defines the deterministic cashflow logic based on an input price path. These are used by pricing and simulation engines in `03_simulations`.

**Each class may also implement a `describe()` or `plot_payoff()` method for intuitive representation and visualization.**

> Note: Payoff functions are deterministic and assume the path is already simulated. Stochastic modeling and Monte Carlo logic are implemented separately.
