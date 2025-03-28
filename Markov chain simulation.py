import numpy as np
import matplotlib.pyplot as plt

def calculateTimeAverages(n, P):
    numOfSteps = n # our large time
    state = randomInitialState() #initial state
    stateCounts = [0, 0, 0] # running count of total visits of each state
    stateTimeAvs = [[],[],[]] # holds each running time average (proportion)
    transitionMatrix = P

    # run the actual simulation and calculates running proportions
    for i in range(numOfSteps):
        state = np.random.choice([0, 1, 2], p=transitionMatrix[state]) # generate random state given current states propabilities
        stateCounts[state] += 1 # adds 1 to new states visit count
        for j in range(3):
            stateTimeAvs[j].append(stateCounts[j]/(i+1)) # appends newn proportions to each states running time average

    return stateTimeAvs


def randomInitialState():
    # generates an array of 3 random numbers that sum to 1 
    
    distribution = np.random.dirichlet([1,1,1])
    initialState = np.random.choice([0, 1, 2], p=distribution)
    
    return initialState


def calculateMovingAverage(A):
    # calculates 3 point moving average of the 3 arrays in array A

    movingAverages = [[],[],[]] # new array to hold the arrays of moving averages
    
    for i in range(3): # iterates over each array in A
        for j in range(1, len(A[i])-1):
            movingAverages[i].append((A[i][j-1]+A[i][j]+A[i][j+1])/3)
            
    return movingAverages


P = [[0.2, 0.6, 0.2], [0.1, 0.5, 0.4], [0.7, 0.1, 0.2]]#Weighted Adjacency (transition) Matrix of markov chain

numOfSteps = 1000000 # number of trials (time) of process   (can be changed to any value n>=1)
runningProportions = calculateTimeAverages(numOfSteps, P)

print([runningProportions[0][-1], runningProportions[1][-1], runningProportions[2][-1]]) # prints finial vector of proportions

timePoints = [x for x in range(0, numOfSteps-2)] #for horizontal axis of plot

# plot results
plt.stackplot(timePoints, calculateMovingAverage(runningProportions), colors = ["b","c","g"])
plt.axhline(0.3, color = "r", linestyle = "dotted", linewidth = 2.5)
plt.axhline(0.3+5/12, color = "r", linestyle = "dotted", linewidth = 2.5)
plt.xlabel("n")
plt.ylabel("Running average of proportions")
plt.title("Convergence of time averages in Markov chain")
plt.show()








