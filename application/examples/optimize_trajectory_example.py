import matplotlib.pyplot as plt
import numpy as np
from python_code import optimize_trajectory

# Parameters for the optimization
fuel_mass = 500000  # Fuel mass in kg
initial_thrust = 20000  # Initial thrust in Newtons
closest_approach_distances = np.linspace(5e6, 2e7, 50)  # Range of distances to visualize costs
optimal_costs = []

# Compute optimal cost for each closest approach distance
for closest_approach in closest_approach_distances:
    _, cost = optimize_trajectory(fuel_mass, initial_thrust, closest_approach)
    optimal_costs.append(cost)

# Plotting the results to observe optimal closest approach distances
plt.figure(figsize=(10, 6))
plt.plot(closest_approach_distances, optimal_costs, color="purple", linestyle="-", marker="o", markersize=5)
plt.xlabel("Closest Approach Distance (m)", fontsize=12)
plt.ylabel("Optimal Cost", fontsize=12)
plt.title("Optimization of Spacecraft Trajectory Costs for Gravitational Assists", fontsize=14)
plt.grid(True, linestyle="--", alpha=0.7)

# Identify and annotate the minimum and maximum cost points
min_cost_index = np.argmin(optimal_costs)
max_cost_index = np.argmax(optimal_costs)

# Annotate minimum cost on the plot
plt.annotate(
    f"Min Cost: {optimal_costs[min_cost_index]:.2f}",
    xy=(closest_approach_distances[min_cost_index], optimal_costs[min_cost_index]),
    xytext=(closest_approach_distances[min_cost_index] * 1.5, optimal_costs[min_cost_index] * 1),
    arrowprops=dict(arrowstyle="->", lw=1.5),
    fontsize=10,
)

# Annotate maximum cost on the plot
plt.annotate(
    f"Max Cost: {optimal_costs[max_cost_index]:.2f}",
    xy=(closest_approach_distances[max_cost_index], optimal_costs[max_cost_index]),
    xytext=(closest_approach_distances[max_cost_index] * 0.3, optimal_costs[max_cost_index] * 0.9),
    arrowprops=dict(arrowstyle="->", lw=1.5),
    fontsize=10,
)

plt.tight_layout()  # Adjust layout for clarity
plt.savefig("plots/optimize_trajectory_plot.png", format="png", dpi=300)
plt.show()  # Display the plot
