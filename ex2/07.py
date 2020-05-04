import matplotlib.pyplot as plt

X1, Y1 = range(0, 10), [61, 45, 27, 88, 47, 61, 45, 27, 88, 47]
X2, Y2 = range(0, 10), [15, 33, 57, 22, 32, 15, 33, 57, 22, 32]
X3, Y3 = range(0, 5), [15, 33, 57, 22, 32]
labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
fig = plt.figure()

ax1 = fig.add_subplot(3,1,1)
ax1.bar(X1, Y1, color = "b", tick_label = labels)
ax1.set_title("dog")

ax2 = fig.add_subplot(3,1,3)
ax2.bar(X2, Y2, color = "g", tick_label = labels)
ax2.set_title("cat")

ax3 = fig.add_subplot(3,3,5)
ax3.bar(X3, Y3, color = "c", tick_label = labels[:5])
ax3.set_title("bird")

plt.tight_layout()
plt.show()