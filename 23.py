with open('test.txt', 'w') as file:
    file.write("1 2\n2 4\n3 1")
x = []
y = []
with open('test.txt', 'r') as file:
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y.append(float(values[1]))
import matplotlib.pyplot as plt

plt.plot(x, y, color="blue", marker="o")
plt.xlabel("x - axis")
plt.ylabel("y - axis")
plt.title("Sample graph!")
plt.show()
