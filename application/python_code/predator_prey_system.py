# Define the predator-prey system as a system of differential equations
def predator_prey_system(populations, t, alpha, beta, delta, gamma):
    """
    Calculate the rate of change for prey and predator populations based on Lotka-Volterra equations.

    Parameters:
    - populations (list): A list with two elements: [prey, predator] populations at time t.
    - t (float): Time variable, required for odeint even though it's unused here.
    - alpha (float): Prey growth rate.
    - beta (float): Rate at which predators consume prey.
    - delta (float): Predator growth rate from consuming prey.
    - gamma (float): Natural predator death rate.

    Returns:
    - list: Contains the rate of change [dprey_dt, dpredator_dt] for prey and predator populations.
    """
    prey, predator = (
        populations  # Unpack the populations array into prey and predator variables
    )
    dprey_dt = alpha * prey - beta * prey * predator  # Rate of change for prey
    dpredator_dt = (
        delta * prey * predator - gamma * predator
    )  # Rate of change for predator
    return [dprey_dt, dpredator_dt]
