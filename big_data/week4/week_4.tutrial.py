import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [1, 3, 2, 4, 5]

# Create a new figure
fig, ax = plt.subplots()

# Plot the data as a line
ax.plot(x, y)

# Add labels and title
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('One-dimensional plot')

# Show the plot
plt.show()
