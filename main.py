
"""
print("I love pizza")
print("Second line wow")
print('Using single quotations')
print("Difference kya hain phir?!")

# we will learn variables now

name = "Abaan"
#print(type(name)) #This will print the datatype of our variable
#print(name)
                                                                                        
first_name = "Abaan"
last_name = "Sarguroh"

full_name = first_name + " " + last_name

print(full_name)

age = 18

print("Hello, "+full_name + ", who is " +str(age) + " years old.")

"""

age = int (input("Enter your age: "))
if age >= 18:
    print("You are an adult ")

elif age == 18:
    print("okayy les go")
else:
    print("poochha?")

while age >=18:
    age = int(input("Enter your age: "))


age = int(input("Enter your age: "))

while age >=18:
    age = int(input("Enter your age: "))


# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = 7

# To take input from the user
#num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)


