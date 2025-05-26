#Products

This folder defines exotic option payoff structures.

Each file implements a specific product type, such as:
- Barrier options (knock-in, knock-out)
- Asian options (arithmetic/geometric)
- Digital/binary options
- Autocallables (vanilla or worst-of)
- Cliquets and path-dependent instruments

Each product exposes a `payoff(path)` method to be used by simulation engines.
