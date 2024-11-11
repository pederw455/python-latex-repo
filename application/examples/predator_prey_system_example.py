import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from python_code import predator_prey_system

# Parameters for the system
alpha = 0.1            # Prey growth rate
beta = 0.02            # Rate at which predators consume prey
delta = 0.01           # Rate at which prey consumption converts into predator growth
gamma = 0.1            # Predator death rate
prey_initial = 40      # Initial population of prey
predator_initial = 9   # Initial population of predators
time = np.linspace(0, 200, 1000)  # Time points for simulation from 0 to 200 in 1000 steps

# Solve the differential equations using the initial conditions and parameters
initial_conditions = [prey_initial, predator_initial]
solution = odeint(predator_prey_system, initial_conditions, time, args=(alpha, beta, delta, gamma))

# Plotting the predator and prey populations over time
plt.figure(figsize=(8, 6))
plt.plot(time, solution[:, 0], label="Prey Population", color="blue", linestyle="-", linewidth=2)
plt.plot(time, solution[:, 1], label="Predator Population", color="red", linestyle="-", linewidth=2)
plt.fill_between(time, solution[:, 0], color="blue", alpha=0.1)
plt.fill_between(time, solution[:, 1], color="red", alpha=0.1)

# Add legend, labels, and grid for clarity
plt.legend(loc="upper right", frameon=True, shadow=True)
plt.title("Predator-Prey Dynamics", fontsize=14)
plt.xlabel("Time", fontsize=12)
plt.ylabel("Population", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)
plt.tight_layout()

plt.savefig('plots/predator_prey_system_plot.png', format='png', dpi=300)
plt.show()