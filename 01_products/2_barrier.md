# Barrier Options

Barrier options are a class of **path dependent exotic derivatives** whose payoffs are dependent on the fullfilling or breaching of a

$$
X_{n+1} = X_n + \Delta t \, \mu(X_n, t_n) 
+ \sum_{i=1}^m \sigma_i(X_n, t_n) \, \Delta W_n^{(i)} 
+ \frac{1}{2} \sum_{i=1}^m \left( \sigma_i(X_n, t_n) \cdot \nabla_x \sigma_i(X_n, t_n) \right) \left( (\Delta W_n^{(i)})^2 - \Delta t \right) 
+ \mathcal{O}((\Delta t)^{3/2})
$$
