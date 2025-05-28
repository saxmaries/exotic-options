# Exotic Options

This project is a personal exploration and implementation of exotic option products, aimed at deepening practical understanding of **structured derivatives** as used on trading desks.

Rather than focusing on abstract quant models, this repo reflects the type of work an **exotic structurer** would do, linking **product payoffs**, **market views**, and **risk considerations** through simulation, visualization, and pricing tools.

---

## Why This Exists

Structured products are widely used in equity and FX markets to tailor yield, manage risk, or reflect investor views. 

This project simulates and prices these products using:
- Realistic **stochastic models** (GBM, Heston),
- Custom **payoff engines** per product,
- and **Monte Carlo simulation** to price and visualize payoff behavior.

It's designed to help answer questions like:
- How does a Phoenix autocall perform under different vol regimes?
- What happens to a knock-in barrier with high skew?
- How do different model assumptions affect hedging risk?

---

## Assumed Knowledge

To follow this repo, you should be comfortable with:
- General finance concepts (equity, fixed income, FX, and basic derivative instruments)
- Vanilla option pricing and the Black-Scholes framework
- Basic stochastic calculus (GBM, volatility surfaces)
- Python and Jupyter

- MFE/MQF candidates highly preferred.

---

## Repo Structure

```bash
.
├── 01_products/         # Product-specific payoff definitions
├── 02_models/           # Underlying model engines (GBM, Heston, etc.)
├── 03_simulations/      # Monte Carlo pricing engine
├── 04_greeks/           # Risk sensitivities
├── 05_notebooks/        # Interactive notebooks for analysis & visualization
