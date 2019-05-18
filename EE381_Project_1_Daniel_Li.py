#EE 381 spring 2019 Project1
#Name: Daniel Li
#ID: 014504891
#Start Date: 1/23/2019
#End Date: 1/6/2019


#This program outputs summary statistics for inputted data
def main():
    L=[]#list for the data
    v=1; #boolean variable set to high state

    print('You will be asked to enter non-negative integers')
    print('When you want to stop, enter a letter')

    while v==1:
        try:
            l=int(input('Enter a non-negative integer:  '))
            while(l<1):
                l=int(input('Invalid input! Enter a non-negative integer:  '))
            L.append(l)
        except ValueError:
            print('Input has been stopped')
            print('\n')
            v=0 #changed logic state
    print('You inputed the list of numbers:  ',L)
    print('\n')
    Mean=mean(L)
    median(L)
    mode(L)
    Range(L)
    Variance=variance(L,Mean)
    standardDeviation(Variance)
    
    
#function to calculate the mean
def mean(L):
    s=sum(L) #calculates the sum of inputted numbers
    N=len(L) #The number of numbers in the list
    mean=s/float(N) #Arithmentic average
    print('The mean of the inputted numbers is, ',mean)
    return mean

#fuction to calculate the median
def median(L):
    L.sort() 
    N=len(L)
    #Even case
    if N%2==0:
        m1=N/2
        m2=m1+1
        m1=int(m1)
        m2=int(m2)
        m1=m1-1   

        median=(L[m1]+L[m2])/2
    #Odd case
    else:
        m=(N+1)/2
        m=int(m)-1
        median=L[m]
    print('The median of the inputted numbers is, ',median)

#function to calculate the mode
def mode(L):
    from collections import Counter
    modes=[]
    c=Counter(L)
    freq=c.most_common()
    max_occur=freq[0][1]
    if max_occur!=1:
        for m in freq:                  
            if m[1]==max_occur:
                modes.append(m[0])
        print ('The mode(s) are: '),
        for p in modes:
            print(str(p),' with frequency ',max_occur)
    else:
        print('There are no modes')

#function to calculate the range
def Range(Y):
    highest = max(Y)
    lowest = min(Y)
    r = highest - lowest
    print(("The range is: "), r)

#function to calculate the variance
def variance(L,u):
    S=0
    N=len(L)
    for n in L:
        x=(n-u)**2
        S=S+x
    variance=S/N
    print('The variance of the inputted numbers is, ',variance)
    return variance

#function to calculate the Standard deviation
def standardDeviation(Variance):
    import math
    stdDeviation=math.sqrt(Variance)
    print('The standard deviation of the inputted numbers is, ',stdDeviation)

main()

print(" ")

debts = [ ["rent",0],["credit",0],["groceries",0], ["Transportation",0]]

for i in debts:
		print(("The debt is: "), i[0])
		i[1] = float(input("Enter the amount of money: "))

debts.sort(key=lambda x: x[1], reverse = True)

import matplotlib.pyplot as pareto

x = []
y = []
for i in debts:
	x .append(i[0])
for i in debts:
	y.append(i[1])

pareto.bar(x,y,1,0)
