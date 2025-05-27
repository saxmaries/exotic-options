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
