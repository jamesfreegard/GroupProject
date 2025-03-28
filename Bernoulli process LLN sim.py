import numpy as np
import matplotlib.pyplot as plt

probability = 0.6 # probability Xn = 1 in bernoulli process   (can be changed to any value in (0,1))
numOfSteps = 5000 # number of trials (time) of process   (can be changed to any value n>=1)
total = 0 # keeps track of running total sum for calculion of sample mean
xBar = [] # array holding running sample mean

# generating the process
for i in range(numOfSteps):
    x = np.random.choice([0, 1], p=[1-probability, probability])
    total += x
    xBar.append(total/(i+1))

# plot of running sample mean
plt.plot(xBar, color = "black")
plt.axhline(probability, color = "red", linestyle = "dotted")
plt.ylabel("Running sample mean")
plt.xlabel("n")
plt.title("Convergence of sample mean of Bernoulli process Bern(0.6)")
plt.show()

