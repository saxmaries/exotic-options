# Asian Options

Asian options are exotic options whose payoffs depend on the **average price** of the underlying asset over a time window. They're often used in structured products to **smooth volatility**, **mitigate market manipulation**, and **reflect long-term views**.

## Types Implemented

- **Arithmetic average** (most commonly used in the market)
- **Geometric average** (used for analytical tractability in testing)
- Both **Call** and **Put** styles supported

## Payoff Examples

- **Arithmetic Asian Call**: `max(Avg(S) - K, 0)`
- **Geometric Asian Put**: `max(K - Geomean(S), 0)`

## Code Usage

```python
from products.asian import AsianOption

option = AsianOption(strike=100, average_type='arithmetic', option_type='call')
option.payoff([95, 98, 100, 105])  # example price path
