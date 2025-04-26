#5. Factorial (Recursive)
#Allowing user to input a number
number=int(input("Enter your number: "))

def factorial(number):
    #defining the base case
    if number==0:
        return 1
    else:
        #defining the recursive case
        return number *factorial(number-1)
print("Factorial of",number,"is:",factorial(number))

