#4. Reverse a string (without using [::-1] or built-in methods).
user_string = input("Enter a string: ")
reversed_string = ""

#for loop to add string letters ahead of reversed string
for l in user_string:
    reversed_string = l + reversed_string
print(reversed_string)