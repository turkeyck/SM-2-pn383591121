import random
import time
import math

def Function(sides1,sides2,sides3,N):
    c1=time.clock()
    print("========================")
    
    print("Number of sides of dice1 = ", sides1)
    print("Number of sides of dice1 = ", sides2)
    print("Number of sides of dice3 = ", sides3)
    print("Throw the dice for N times ,N =",N)


    print("-----Simulation(S)-----")

    #Histogram records the sum of dice numbers 

    histogram = []
    for s in range(N):
        histogram.append(0) 
    print("Initialization")
    print(histogram)

    #Histogram2 records the number of events of dice sum 

    histogram2 = []
    for s in range(sides1+sides2+sides3):
        histogram2.append(0)
    print(histogram2)
 
    
    r = 0
    r1 = 0
    r2 = 0
    r3 = 0
    
    for t in range(N):
        r1 = int(random.random()*sides1)+1 # dice 1 number
        r2 = int(random.random()*sides2)+1 # dice 2 number
        r3 = int(random.random()*sides3)+1 # dice 3 number 
        histogram[t] = r1+r2+r3
        r = r1 + r2 +r3 -1
        histogram2[r] = histogram2[r] + 1
    print("After N trials , the sum of dice number.")
    print(histogram)
    print("Distribution for the sum of dice [1,2,3...]")
    print(histogram2)
    
    print("-----Simulation(E)-----")

    print("-----Analysis(S)-------")

    histogram3 = []
    for s in range(sides1+sides2+sides3):
        histogram3.append(0)
        histogram3[s] = histogram2[s] / (N)
    #histogram3 shows the probability distrobution of the trials
    print("Probability distribution for the sum of two dice [1,2,3...]")
    print(histogram3)
    
 

    
    print("-----Analysis(E)-------")

    print("========================")
  

def run():

    Function(6,8,10,100)


run()
