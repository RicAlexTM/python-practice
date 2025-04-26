#2. Check if a number is even or odd.
#Allowing user to enter a certain number
number=int(input("Enter your number:"))

#Checking the type of number
if number%2==0:
    print(number,"is even")
else:
    print(number,"is odd")