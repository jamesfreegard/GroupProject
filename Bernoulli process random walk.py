import numpy as np
import matplotlib.pyplot as plt

probability = 0.35 # probability Xn = 1 in bernoulli process   (can be changed to any value in (0,1))
sample_path = [] # array holding the sample path
x_axis = [] # for the plot
n = 10 # number of trials (time) in sample path   (can be changed to any value n>=1)


# generating the sample path
for i in range(n):
    x = np.random.choice([0, 1], p=[1-probability, probability])
    sample_path.append(x)
    x_axis.append(i)


# below plots the sample path
plt.scatter(x_axis,sample_path, label = "sample path")
plt.xticks(range(0,n))
plt.yticks(range(0,2))
plt.ylim(-0.2,1.5)
plt.xlabel("n")
plt.ylabel("Xn")
plt.title("Sample path of bernoulli process")
plt.show()
