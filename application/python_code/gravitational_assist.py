import numpy as np

# Function to calculate the final velocity of a spacecraft after gravitational assist
def gravitational_assist(spacecraft_velocity, planet_velocity, planet_mass, closest_approach_distance):
    """
    Calculate the final velocity of a spacecraft after a gravitational assist with a planet.

    Parameters:
    - spacecraft_velocity (float): Initial velocity of the spacecraft in m/s.
    - planet_velocity (float): Velocity of the planet in m/s.
    - planet_mass (float): Mass of the planet in kg.
    - closest_approach_distance (float): Distance of closest approach in meters.

    Returns:
    - v_final (float): The spacecraft's final velocity after the gravitational assist.
    """
    G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2

    # Relative initial velocity between the spacecraft and the planet
    v_rel_initial = abs(spacecraft_velocity - planet_velocity)

    # Calculate velocity at infinity (far from the planet) after gravitational interaction
    v_inf = np.sqrt(v_rel_initial**2 + 2 * G * planet_mass / closest_approach_distance)

    # Calculate final velocity considering energy changes from the approach and assist
    v_final = np.sqrt(spacecraft_velocity**2 + 2 * (v_inf**2 - spacecraft_velocity * v_inf * np.cos(np.pi)))

    return v_final
