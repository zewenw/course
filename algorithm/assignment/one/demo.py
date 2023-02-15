import matplotlib.pyplot as plt

# Define two arrays of x and y coordinates
x = [1, 2, 3, 4, 5]
y = [2, 4, 3, 5, 1]

# Create a plot with the given coordinates
plt.plot(x, y, 'bo')

# Set the x and y axis limits
plt.xlim(0, 6)
plt.ylim(0, 6)

# Add axis labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Coordinate Map')

# Add text annotation for each point's coordinates
for i in range(len(x)):
    plt.text(x[i] + 0.1, y[i] + 0.1, f'({x[i]}, {y[i]})')

# Show the plot
plt.show()
