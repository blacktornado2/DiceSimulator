import random

#Function Fair Die which uses random module and selects a number b/w 1 and 6(both included), and shows it to the user 
#Function used : random.randit(a,b)
def FairDie():
    print("Great, A fare die. How many iterations do you want to see of this fair die : ")
    iterations = int(input())
    print(f"Ok ! Here are your {iterations} iterations : ",end="")
    for i in range(iterations):
        number = random.randint(1,6)
        print(number,end=" ")

    del iterations


#In case of a biased die we will ask the user, which number's probabilty user wants to get biased
def BiasedDie():
    print("Good choice, a biased die... ")
    biasedNumber = int(input("Which number's probability do you want to get biased: "))

    while biasedNumber < 1 or biasedNumber > 6:
        biasedNumber = int(input("Incorrect input ! Please enter a valid number b/w 1 to 6 (both inclusive): "))            #biasedNumber input validation

    ProbabilityBiased = float(input("Enter the probablity of that biased number (b/w 0-100%): "))
    while ProbabilityBiased < 0.00 or ProbabilityBiased >100.00:
        ProbabilityBiased = float(input(f"Wrong input! Enter the probablity of {biasedNumber} (b/w 0-100%): "))             #ProbabilityBiased input validation

    ProbabilityBiased = ProbabilityBiased/100                                                                               #Converting the probability to 0.00-1.00

    iterations = int(input("ALright, How many iterations do you want to see of this biased die : "))                        #Taking no. of iterations as input from the user
    ProbabilityLeft = 1.00 - ProbabilityBiased                                                                              #Probability left is the total probabilty left of unbiased numbers
    
    EachNumberProbabilty = ProbabilityLeft / 5                                                                              #Probability left is divided into each unbiased number
    
    NumbersOfDie = [0,1,2,3,4,5,6]
    Weights = [0,EachNumberProbabilty,EachNumberProbabilty,EachNumberProbabilty,EachNumberProbabilty,EachNumberProbabilty,EachNumberProbabilty]
    
    Weights[biasedNumber] = ProbabilityBiased
    
    BiasedList = random.choices(NumbersOfDie,weights = Weights,k = iterations)                                              #random.choices() returns us the list with probabilties according to the weights list given as input
    
    print(f"Ok ! Here are your {iterations} iterations ")
    for i in range(1,len(BiasedList)):                                                                                      #Printing the iterations
        print(BiasedList[i],end=" ")

    del BiasedList,biasedNumber,ProbabilityBiased,iterations,NumbersOfDie,Weights                                           #Deleting the created variables after they are used (Memory Management)

if __name__ == "__main__":
    while(True):
        print("\n\n\n**********    Welcome to Dice Simulator    **********\n\n")
        print("What type of die do you want to roll :")
        print("1. Fair Die \n2. Biased Die\n3. Exit the Simulator")
        x = int(input("Enter you choice : "))

        if x == 1:
            FairDie()

        elif x == 2:
            BiasedDie()

        elif x == 3:
            break

        else:
            print("Wrong Input! Please enter a valid Number !! ")
    
    