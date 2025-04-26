#3. Compute factorial using a loop.
#Allowing user to input a number
number=int(input("Enter your number: "))

factorial=1
#for loop to find the factorial of the number
for i in range (1,number+1):
    if number==0:
        print("factorial of " ,number, "is:" ,1)
    else:
        factorial=factorial*i

print("factorial of",number, "is:",factorial)