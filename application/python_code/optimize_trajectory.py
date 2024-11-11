import numpy as np
from scipy.optimize import minimize


# Function to optimize the spacecraft's trajectory based on fuel efficiency and gravitational assist
def optimize_trajectory(fuel_mass, initial_thrust, closest_approach):
    """
    Objective function for trajectory optimization using gravitational assist.

    Parameters:
    - fuel_mass (float): Total mass of fuel onboard in kg.
    - initial_thrust (float): Initial thrust in Newtons.
    - closest_approach (float): Closest approach distance to the celestial body in meters.

    Returns:
    - Optimal parameters (list): [time, thrust] values that minimize the cost function.
    - Cost (float): Minimized cost function value.
    """

    # Define the cost function for optimization
    def objective(params):
        time, thrust = params  # Unpack parameters: time and thrust

        # Calculate delta-v (velocity change) based on thrust and time
        delta_v = thrust * time / fuel_mass

        # Calculate the effect of gravitational assist based on closest approach distance
        gravitational_assist_effect = np.log(closest_approach) if closest_approach > 1 else 0

        # Simulate distance traveled using delta-v and gravitational effect
        distance_traveled = delta_v * time * gravitational_assist_effect / 2

        # Calculate the cost considering fuel usage, time penalty, and gravitational assist efficiency
        fuel_used = fuel_mass - (thrust * time) / delta_v
        time_penalty = 0.05 * time**1.2  # Small non-linear penalty for extended time
        efficiency_penalty = 0.01 * (closest_approach - 7e6) ** 2  # Optimal closest approach is around 7 million meters

        # Total cost combines all penalties and fuel usage
        cost = fuel_used + time_penalty + efficiency_penalty
        return cost

    # Initial guess for time and thrust
    initial_guess = [1e6, initial_thrust]

    # Define bounds for time and thrust to avoid unrealistic values
    bounds = [(1e5, 1e7), (5000, 3e5)]

    # Minimize the objective function to find the optimal time and thrust
    result = minimize(objective, initial_guess, bounds=bounds)
    return result.x, result.fun  # Return optimal parameters and the minimized cost
