import matplotlib.pyplot as plt
import numpy as np
from python_code import calculate_hohmann_transfer

# Parameters
earth_orbit_radius = 1.496e11  # Radius of Earth's orbit in meters
mars_orbit_radius = 2.279e11  # Radius of Mars's orbit in meters
delta_v_earth, delta_v_mars, total_delta_v = calculate_hohmann_transfer(earth_orbit_radius, mars_orbit_radius)

# Generate coordinates for Earth's and Mars's orbits
theta = np.linspace(0, 2 * np.pi, 100)
earth_orbit_x = earth_orbit_radius * np.cos(theta)
earth_orbit_y = earth_orbit_radius * np.sin(theta)
mars_orbit_x = mars_orbit_radius * np.cos(theta)
mars_orbit_y = mars_orbit_radius * np.sin(theta)

# Transfer orbit parameters
a_transfer = (earth_orbit_radius + mars_orbit_radius) / 2  # Semi-major axis of transfer orbit
e_transfer = (mars_orbit_radius - earth_orbit_radius) / (earth_orbit_radius + mars_orbit_radius)  # Eccentricity

# Generate coordinates for the Hohmann transfer orbit
transfer_orbit_x = a_transfer * (np.cos(theta) - e_transfer)
transfer_orbit_y = a_transfer * np.sqrt(1 - e_transfer**2) * np.sin(theta)

# Plot the orbits and the transfer path
plt.figure(figsize=(8, 8))
plt.plot(earth_orbit_x, earth_orbit_y, label="Earth Orbit", color="blue", linestyle="-")
plt.plot(mars_orbit_x, mars_orbit_y, label="Mars Orbit", color="red", linestyle="-")
plt.plot(transfer_orbit_x, transfer_orbit_y, "--", label="Transfer Orbit", color="green")
plt.scatter([0], [0], color="yellow", s=200, edgecolor="orange", label="Sun")

# Plot styling
plt.legend(loc="upper right", frameon=True, shadow=True)
plt.title(f"Hohmann Transfer Orbit\nTotal Δv = {total_delta_v:.2f} m/s", fontsize=14)
plt.xlabel("Distance (m)", fontsize=12)
plt.ylabel("Distance (m)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.axis("equal")
plt.savefig("plots/calculate_hohmann_transfer_plot.png", format="png", dpi=300)
plt.show()
