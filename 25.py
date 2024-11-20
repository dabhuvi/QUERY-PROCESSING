import matplotlib.pyplot as plt
x = [10, 20, 30]
y1 = [10, 30, 10]
y2 = [40, 20, 40]
plt.plot(x, y1, color='blue', linewidth=3, label='line1-width-3')
plt.plot(x, y2, color='red', linewidth=5, label='line2-width-5')
plt.title('Two or more lines with different widths and colors with suitable legends')
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.legend()
plt.show()
