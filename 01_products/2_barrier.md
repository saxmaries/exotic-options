# Barrier Options

Barrier options are a class of **path dependent exotic derivatives** whose payoffs are dependent on the fullfilling or breaching of a

$$
X_{n+1} = X_n + \Delta t \cdot \mu\left(X_n, t_n\right) + \sum_{i=1}^m \sigma_i\left(X_n, t_n\right) \cdot \Delta W_n^{(i)} + \frac{1}{2} \sum_{i=1}^m \left( \sigma_i\left(X_n, t_n\right) \cdot \nabla_x \sigma_i\left(X_n, t_n\right) \right) \cdot \left( \left( \Delta W_n^{(i)} \right)^2 - \Delta t \right) + \mathcal{O}\left( (\Delta t)^{3/2} \right)
$$

