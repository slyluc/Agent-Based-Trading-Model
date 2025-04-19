import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Ensure 3D plotting support

# --- Load the CSV Data ---
df = pd.read_csv("../Data/simulation_results1820runsVECTORIZED5.csv")

# --- Average over the 10 runs ---
# Group by U_value and sigma_value and compute the mean for hurst_exponent and fraction_need.
avg_df = df.groupby(["U_value", "sigma_value"], as_index=False).agg({
    "hurst_exponent": "mean",
    "fraction_need": "mean"
})

# --- Pivot the Data ---
# Create a pivot table so that rows represent sigma values, columns represent U values.
hurst_pivot = avg_df.pivot(index="sigma_value", columns="U_value", values="hurst_exponent")
frac_need_pivot = avg_df.pivot(index="sigma_value", columns="U_value", values="fraction_need")

# --- Create Meshgrid for the 3D Plot ---
# Extract the sorted unique U values (columns) and sigma values (index)
U = hurst_pivot.columns.values
sigma = hurst_pivot.index.values
U_grid, sigma_grid = np.meshgrid(U, sigma)

# Get the 2D arrays of values to plot for each surface
Z_hurst = hurst_pivot.values      # Average Hurst exponent surface
Z_frac_need = frac_need_pivot.values  # Average Fraction Need surface

# --- Plotting the 3D Surfaces ---
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")


# Plot the average fraction need surface with a different color map (plasma)
surf2 = ax.plot_surface(U_grid, sigma_grid, Z_frac_need, cmap="plasma", alpha=0.8, edgecolor="none")
# Plot the average Hurst exponent surface with one color map (viridis)
surf1 = ax.plot_surface(U_grid, sigma_grid, Z_hurst, cmap="viridis", alpha=0.8, edgecolor="none")



# Label the axes and add a title.
ax.set_xlabel("U")
ax.set_ylabel(r"$\sigma$")
ax.set_zlabel("Value")
ax.set_title(r"3D Surface Plot: U vs $\sigma$ vs Average Hurst & Fraction Need")
ax.set_zlim(0,1.1)
# Add color bars for each surface. Note that having two colorbars in one plot is acceptable,
# but you might consider adjusting the positions if needed.
cbar1 = fig.colorbar(surf1, shrink=0.5, aspect=10, pad=0.1)
cbar1.set_label("Avg Hurst Exponent")
cbar2 = fig.colorbar(surf2, shrink=0.5, aspect=10, pad=0.05)
cbar2.set_label("Avg Fraction Need")

plt.show()
