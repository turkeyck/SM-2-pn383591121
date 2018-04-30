import random
import time
import math

def Function(sides,diceNum):
    c1=time.clock()
    print("========================")
    
    print("Number of sides = ", sides)
    print("Number of dice = ", diceNum)

    print("-----Simulation(S)-----")

 

    histogram = []
    for s in range(diceNum):
        histogram.append(0)
    print("Initializatin")
    print(histogram)
    
    

    r = 0
    for t in range(diceNum):
        r = int(random.random()*sides)+1
        histogram[t] = r
    print("After trial")
    print(histogram)
    
    print("-----Simulation(E)-----")

    print("-----Analysis(S)-------")


    Ssum = 0
    Ssqsum = 0
    for x in range(diceNum):
        Ssum += histogram[x]
        Ssqsum += histogram[x]*histogram[x]

    mean = Ssum/diceNum
    variance = Ssqsum/diceNum - mean*mean
    deviation = math.sqrt(variance)

    mean_theo = (sides + 1)/2
    variance_theo = (sides*sides -1)/12
    deviation_theo = math.sqrt(variance_theo)
    
    print("Sum(simulation) , mean(simulation) , variance(simulation) , deviation(simulation) ")
    print(Ssum ,mean ,variance ,deviation)
    print("mean(theory) , variance(theory) , deviation(theory)")
    print(mean_theo ,variance_theo ,deviation_theo)
    print("deviation from theory")
    print(mean_theo-mean ,variance_theo-variance ,deviation_theo-deviation)
    print("deviation from theory(%)")
    print((mean_theo-mean)/mean_theo*100 ,(variance_theo-variance)/variance_theo*100 ,(deviation_theo-deviation)/deviation_theo*100)   

    
    print("-----Analysis(E)-------")

    print("========================")
  

def run():

    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)
    Function(2, 5)



run()
