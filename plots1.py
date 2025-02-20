import matplotlib.pyplot as plt

# Create a figure with 20 subplots arranged in a 5x4 grid
fig, ax = plt.subplots(nrows=5, ncols=4)

# Iterate over the subplots
for i in range(5):
    for j in range(4):
        # Plot something on each subplot
        ax[i, j].plot([1, 2, 3], [4, 5, 6])
        ax[i, j].set_title(f'Subplot {i+1},{j+1}')

# Adjust the spacing between subplots
plt.tight_layout()

# Display the figure
plt.show()
