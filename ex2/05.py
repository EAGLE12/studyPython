import matplotlib.pyplot as plt
X = [num*100 for num in range(1,6)]
Y1 = [40, 65, 80, 50, 20]
Y2 = [50, 35, 30, 55, 25]
Y3 = [80, 25, 40, 80, 80]
plt.plot(X, Y1, marker="o", linestyle = "-", label = "Y1")
plt.plot(X, Y2, marker="v", linestyle = "--", label = "Y2")
plt.plot(X, Y3, marker="^", linestyle = "-.", label = "Y3")

plt.grid()
plt.legend(loc = "best")
plt.show()
print(X)