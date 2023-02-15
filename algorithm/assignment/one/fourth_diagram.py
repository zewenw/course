import matplotlib.pyplot as plt

# Define the coordinates of the points you want to plot
x = [1, 1, 6, 6]
y = [0, 3, 3, 0]

# Create a scatter plot with the given coordinates
plt.plot(x, y)

# Set the x and y axis limits
plt.xlim(0, 7)
plt.ylim(0, 5)

# Add axis labels and a title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Fourth Envelope')

# Add text on diagram
# for i in range(len(x)):
#     plt.text(x[i] + 0.1, y[i] + 0.1, f'({x[i]}, {y[i]})')

# for xi, yi in zip(x, y):
#     # print(f'x={xi}, y={yi}')
#     plt.text(x, y, f'({xi}, {yi})', ha='center', va='bottom')
plt.text(3, 4, '(1,3),(6,0)', fontsize=12)

# Show the plot
plt.show()
