# python program simple calculator


# function to add two numbers
def Add(num1 , num2):
    return num1 + num2

# function to subtract two numbers
def subtract(num1 , num2):
    return num1 - num2

# function to Multiply two numbers
def Multiply(num1 , num2):
    return num1 * num2

# function to Divide two numbers
def Divide(num1 , num2):
    return num1 / num2

print("Please select operation -\n"
      "1. Addition\n"
      "2. Subtraction\n"
      "3. Multiplication\n"
      "4. Divide\n")

# Take input from the user 

select = int(input("Select operation from 1, 2, 3, 4 : "))

number_1 = int(input("Enter a first number = "))
number_2 = int(input("Enter a second number = "))


if (select == 1):
    print(number_1, "+", number_2, "=", Add(number_1, number_2))

elif (select == 2):
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))

elif (select == 1):
    print(number_1, "+", number_2, "=", Multiply(number_1, number_2))

elif (select == 1):
    print(number_1, "+", number_2, "=", Divide(number_1, number_2))

else:
    print("Invalid input ")