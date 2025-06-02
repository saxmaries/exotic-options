# Digital Options

Digital options, also known as **binary options**, are a class of **discontinuous derivatives** where the payoff is a **fixed amount** (or fixed asset value), rather than a function of how far in-the-money the option finishes. These instruments are defined by an **if-then payout structure**, making them distinct from vanilla options, which exhibit continuous payoff sensitivity.

Because of their binary nature, digital options are frequently used to **express precise views** on market levels, **construct high-convexity trades**, or **build structured payouts** that cannot be replicated with simple linear instruments. Their simplicity in outcome is matched by **complexity in risk management**, especially around barrier regions or when path-dependency is involved.

The key variants in practice include:
- **Cash-or-Nothing Calls/Puts:** Fixed payout if terminal spot breaches a strike
- **Asset-or-Nothing Calls/Puts:** Underlying asset delivered if in-the-money
- Gap Options

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

---

## Payoff Mechanics and Formulas

Digital options exhibit **discrete payoffs** based on whether specific conditions are satisfied. Unlike vanilla options, which reward increasing moneyness, digital options deliver a **fixed payout**—often in cash or units of the underlying asset—regardless of how far in- or out-of-the-money the option finishes.

Depending on the product type, digital options may trigger based on **terminal spot**, **barrier touch during the life**, or **absence of touch**. This creates a diverse family of contracts that differ significantly in their path-dependency, hedging profile, and market usage.

---

### Cash-or-Nothing Option

A cash-or-nothing digital option pays a **fixed cash amount** $Q$ if the terminal spot breaches the strike price $K$.

#### Call:

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } S_T > K \\
0, & \text{otherwise}
\end{cases}
$$

#### Put:

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } S_T < K \\
0, & \text{otherwise}
\end{cases}
$$

These are commonly used to express *pure directional bets* or define binary coupon structures within structured notes.

---

### Asset-or-Nothing Option

An asset-or-nothing option pays **the terminal spot price** $S_T$ (instead of a fixed cash amount) if the option finishes in-the-money.

#### Call:

$$
\text{Payoff} = 
\begin{cases}
S_T, & \text{if } S_T > K \\
0, & \text{otherwise}
\end{cases}
$$

#### Put:

$$
\text{Payoff} = 
\begin{cases}
S_T, & \text{if } S_T < K \\
0, & \text{otherwise}
\end{cases}
$$

While less common in practice than cash-based digitals, asset-or-nothing options are analytically useful and play a role in static replication of vanilla options.

---

### One-Touch Option

A one-touch option pays a **fixed amount** $Q$ **if the underlying ever touches or breaches a barrier** $B$ during the option’s life.

#### Up-and-Touch:

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } \exists\, t \in [0,T] \text{ such that } S_t \geq B \\
0, & \text{otherwise}
\end{cases}
$$

#### Down-and-Touch:

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } \exists\, t \in [0,T] \text{ such that } S_t \leq B \\
0, & \text{otherwise}
\end{cases}
$$

This option is **path-dependent**, and in practice may be settled either:
- **Immediately upon touching** (American-style)
- **At expiry** if touch occurred (European-style payout)

One-touch options are sensitive to **volatility**, **barrier proximity**, and **time decay**, and are often used to build *leveraged, short-dated yield products* in FX markets.

---

### No-Touch Option

A no-touch option pays a fixed amount $Q$ **only if the barrier is never touched** during the life of the option.

#### Up-and-No-Touch:

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } \forall\, t \in [0,T] \text{ such that } S_t < B \\
0, & \text{otherwise}
\end{cases}
$$

#### Down-and-No-Touch:

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } \forall\, t \in [0,T] \text{ such that } S_t > B \\
0, & \text{otherwise}
\end{cases}
$$

These options are popular in **range-bound or low-volatility** environments and form the basis of many *structured notes with capital preservation and coupon conditions*.

---

### Double No-Touch Option

This structure pays a fixed amount only if the underlying **stays within a price corridor** for the entire life of the option.

#### Payoff:

Let $L$ and $H$ be the lower and upper barriers, respectively.

$$
\text{Payoff} = 
\begin{cases}
Q, & \text{if } S_t \in (L, H) \text{ for all } t \in [0,T] \\
0, & \text{otherwise}
\end{cases}
$$

Double no-touch options are widely used in:
- **FX range accruals**
- **Capital-at-risk notes**
- **Accrual-based yield notes** with corridor triggers

They are especially sensitive to **volatility skew**, **barrier distance**, and **time to expiry**.

---

### Double One-Touch Option

A double one-touch option pays a fixed amount $Q$ if the spot touches **either** the upper or lower barrier before expiry.

#### Payoff:

Let $L$ and $H$ be the lower and upper barriers, respectively.

$$
\text{Payoff} =
\begin{cases}
Q, & \text{if } \exists\, t \in [0,T] \text{ such that } S_t \leq L \text{ or } S_t \geq H \\
0, & \text{otherwise}
\end{cases}
$$

This structure is used to express **breakout views**, especially in FX or event-driven contexts.

It can be thought of as the **sum of an up-and-touch and a down-and-touch**, and is particularly sensitive to **volatility** and **barrier proximity**.

While less common in structured retail notes, it is frequently used in **volatility-linked products**, **tactical trading**, or **replication-based strategies**.

---

Each of these payoff types introduces unique pricing and hedging considerations, often requiring **closed-form solutions (where available)** or **Monte Carlo simulation** when embedded within complex structured products.

In the following sections, we’ll explore their **Greek sensitivities**, **modeling considerations**, and **Python class interface** for deterministic pricing.

