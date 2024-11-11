import matplotlib.pyplot as plt
from python_code import gravitational_assist

# Define initial parameters for the gravitational assist scenario
spacecraft_velocity = 1.2e4  # Initial velocity of the spacecraft in m/s
planet_velocity = 2.4e4  # Velocity of the planet in m/s
planet_mass = 5.972e24  # Mass of the planet, assuming Earth, in kg
closest_approach_distance = 6.7e6  # Closest approach distance in meters

# Compute the final velocity after gravitational assist
v_final = gravitational_assist(spacecraft_velocity, planet_velocity, planet_mass, closest_approach_distance)

# Prepare data for plotting
velocities = [spacecraft_velocity, planet_velocity, v_final]  # List of velocities to display
labels = ["Initial Spacecraft Velocity", "Planet Velocity", "Final Spacecraft Velocity after Assist"]  # Labels for each bar
colors = ["dodgerblue", "orange", "green"]  # Colors for each bar

# Plot the velocities as a bar chart
plt.figure(figsize=(8, 6))  # Set the figure size
bars = plt.bar(labels, velocities, color=colors, edgecolor="black", linewidth=1.2)  # Create bars with edge styling
plt.ylabel("Velocity (m/s)", fontsize=12)  # Label the y-axis
plt.title("Gravitational Assist Velocity Change", fontsize=14)  # Title of the plot

# Add velocity values on top of each bar for clarity
for bar, velocity in zip(bars, velocities):
    yval = bar.get_height()  # Get the height of each bar to place text
    plt.text(bar.get_x() + bar.get_width() / 2, yval + 500, f"{yval:.2f} m/s", ha="center", va="bottom", fontsize=10)

# Add a grid for the y-axis and adjust layout for clarity
plt.grid(axis="y", linestyle="--", alpha=0.7)  # Grid with dashed lines for the y-axis
plt.tight_layout()  # Adjust layout to prevent clipping
plt.savefig("plots/gravitational_assist_plot.png", format="png", dpi=300)
plt.show()  # Display the plot
