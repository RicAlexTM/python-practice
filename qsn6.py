#6. Sum of Digits of a Number

number=int(input("Enter a number: "))
digit_sum=0

for d in str(number):
    digit_sum+=int(d)
print("sum of digits of",number,"is",digit_sum)
