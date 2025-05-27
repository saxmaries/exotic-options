# Digital Options

Digital options, also known as **binary options**, are a class of **discontinuous derivatives** where the payoff is a **fixed amount** (or fixed asset value), rather than a function of how far in-the-money the option finishes. These instruments are defined by an **if-then payout structure**, making them distinct from vanilla options, which exhibit continuous payoff sensitivity.

Because of their binary nature, digital options are frequently used to **express precise views** on market levels, **construct high-convexity trades**, or **build structured payouts** that cannot be replicated with simple linear instruments. Their simplicity in outcome is matched by **complexity in risk management**, especially around barrier regions or when path-dependency is involved.

The key variants in practice include:
- **Cash-or-Nothing Calls/Puts:** Fixed payout if terminal spot breaches a strike
- **Asset-or-Nothing Calls/Puts:** Underlying asset delivered if in-the-money
- **One-Touch Options:** Pays once if a barrier is touched any time before expiry
- **No-Touch Options:** Pays only if a barrier is *never* breached
- **Double No-Touch Options:** Pays if spot remains within a corridor throughout the life of the option

---

## Common Use Cases

Digital structures are particularly effective when the goal is **to monetize binary outcomes**, **target volatility pricing**, or **build tailored payoffs**. They appear in a variety of asset classes:

- **FX Structured Products**  
  - One-touch options used in *yield-enhancing deposits* or *autopilot yield notes*  
  - Double no-touch notes used in *range-bound carry strategies*

- **Equity-Linked Notes**  
  - Cash-or-nothing digital coupons tied to index or stock-level binary triggers  
  - Autocall structures with embedded one-touch rebates

- **Commodities / Rates**  
  - Range-based accruals for *oil hedging* or *interest rate targeting*  
  - Path-dependent rebate structures for callable bonds

---

## Structuring Motivation

Digital payoffs are attractive tools for both investors and issuers looking to fine-tune exposure and cost. Structurers may include digitals in a product for reasons such as:

- **Yield Enhancement**  
  - One-touch and no-touch coupons offer high premium income in range-bound or low-volatility environments.

- **Cost Reduction**  
  - Embedding a cash-or-nothing put with knock-in behavior reduces overall structure cost while maintaining downside participation.

- **Directional Targeting**  
  - Allows clients to express *precise tactical views*, e.g., “If EUR/USD ever touches 1.15, pay me 10%.”

- **Barrier Risk Monetization**  
  - Traders can exploit volatility skew and forward curve shape by structuring payouts around unlikely barrier events.

- **Discrete Trigger Design**  
  - Useful in retail notes or insurance-wrapped structures where investors want simple yes/no outcomes without tracking mark-to-market.

---

## Desk-Level Integration

From a trading desk perspective, digital options are both **building blocks** and **risk management challenges**. While simple in form, they introduce **nonlinear sensitivities** and require careful monitoring, particularly near barrier levels or during expiry week.

Digitals are embedded in a wide range of structured products:

- **Dual-currency deposits** with embedded one-touch conversion triggers  
- **Auto-callable equity notes** where digital barriers determine coupon or redemption eligibility  
- **Range accrual notes** in FX and rates that pay based on digital corridor logic  
- **Capital-protected notes** featuring cash-or-nothing digital overlays

Desk pricing models must handle the **explosive gamma and vega** around barrier levels, as even small spot movements can produce discontinuous valuation shifts. Static replication may be possible for some digital types (e.g., cash-or-nothing with vanillas and digitals), but dynamic hedging is required for path-dependent types like one-touch.

Digital options are especially popular in **emerging market FX desks**, **private banking flow desks**, and **retail derivatives issuance platforms**, where payout simplicity and headline yield matter more than convexity or hedge efficiency.
