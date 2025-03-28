import numpy as np
import matplotlib.pyplot as plt



probability = 0.35
##n_values = [10, 1000, 100000]
##total = 0
sample_path = []
x_axis = [] #for the plot
n = 10

##for n in n_values:
##    for i in range(n):
##        x = np.random.choice([0, 1], p=[1-probability, probability])
##        total += x
##        if n == 10:
##            sample_path.append(x)
##            x_axis.append(i)
##    print("For n = "+str(n)+" : Sample mean = "+str(round(total/n,5)))
##    total = 0

for i in range(n):
    x = np.random.choice([0, 1], p=[1-probability, probability])
    sample_path.append(x)
    x_axis.append(i)

plt.scatter(x_axis,sample_path, label = "sample path")

plt.xticks(range(0,n))
plt.yticks(range(0,2))
plt.ylim(-0.2,1.5)
plt.xlabel("n")
plt.ylabel("Xn")
plt.title("Sample path of bernoulli process")
plt.show()
