import numpy as np


def calculate_hohmann_transfer(earth_orbit_radius, mars_orbit_radius):
    """
    Calculate the delta-v (velocity change) required for a Hohmann transfer orbit from Earth to Mars.

    Parameters:
    - earth_orbit_radius (float): Radius of Earth's orbit around the Sun in meters.
    - mars_orbit_radius (float): Radius of Mars's orbit around the Sun in meters.

    Returns:
    - delta_v_earth (float): Delta-v required to escape Earth's orbit and enter the transfer orbit.
    - delta_v_mars (float): Delta-v required to enter Mars's orbit from the transfer orbit.
    - total_delta_v (float): Total delta-v for the entire transfer.
    """

    # Gravitational constant for the Sun in m^3/s^2
    mu_sun = 1.32712440018e20

    # Calculate orbital velocities of Earth and Mars using circular orbit approximation
    v_earth = np.sqrt(mu_sun / earth_orbit_radius)  # Velocity of Earth in its orbit
    v_mars = np.sqrt(mu_sun / mars_orbit_radius)  # Velocity of Mars in its orbit

    # Calculate the semi-major axis of the Hohmann transfer orbit (average distance between Earth and Mars)
    transfer_orbit_semi_major_axis = (earth_orbit_radius + mars_orbit_radius) / 2

    # Calculate the velocity required at Earth's position for the transfer orbit
    v_transfer_at_earth = np.sqrt(2 * mu_sun / earth_orbit_radius - mu_sun / transfer_orbit_semi_major_axis)

    # Calculate the velocity required at Mars's position for the transfer orbit
    v_transfer_at_mars = np.sqrt(2 * mu_sun / mars_orbit_radius - mu_sun / transfer_orbit_semi_major_axis)

    # Delta-v at Earth: difference between the transfer orbit velocity and Earth's orbital velocity
    delta_v_earth = v_transfer_at_earth - v_earth

    # Delta-v at Mars: difference between Mars's orbital velocity and the transfer orbit velocity at Mars
    delta_v_mars = v_mars - v_transfer_at_mars

    # Total delta-v required for the Hohmann transfer (sum of absolute delta-v values at Earth and Mars)
    total_delta_v = abs(delta_v_earth) + abs(delta_v_mars)

    return delta_v_earth, delta_v_mars, total_delta_v
