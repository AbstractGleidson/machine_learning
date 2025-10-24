from quadraticFuction import quadraticFunction

def costFuction(x, y, a, b, c):
    """
    Args:
        x (array of numbers): arrays of numbers for axis x
        y (array of numbers): arrays of numbers for axis y
        a (number): coefficient a 
        b (number): coefficient b
        c (number): coefficitent c

    Returns:
        number: Sum of cost
    """
    
    m = x.shape[0] # number of elements
    # calculates all y points for cofficients values
    f_ab = quadraticFunction(x, a, b, c) 
    
    cost_sum = 0
    
    # Sum cost
    for i in range(m):
        cost_sum = (f_ab[i] - y[i]) ** 2 
        
    cost_sum = (cost_sum / m) # avarege of cost
    
    return cost_sum # cost 