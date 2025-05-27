# Barrier Options

Barrier options are a class of **path dependent exotic derivatives** whose payoffs are dependent on the activation or breaching of a barrier.

$$
\text{Discretized Heston Model:}
$$

$$
S_{n+1} = S_n + \mu S_n \Delta t + \sqrt{v_n} S_n \Delta W_n^{(1)}
$$

$$
v_{n+1} = v_n + \kappa \left( \theta - v_n \right) \Delta t + \sigma \sqrt{v_n} \Delta W_n^{(2)}
$$

$$
\text{with} \quad \mathbb{E}\left[\Delta W_n^{(1)} \cdot \Delta W_n^{(2)}\right] = \rho \Delta t
$$
