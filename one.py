print("Hello World")
a=5
b=7
c=a+b
print(c)
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")
for number in range (1,11):
    print(number)


def find_largest(num1, num2, num3):
    if num1 >= num2:
        if num1 >= num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 >= num3:
            largest = num2
        else:
            largest = num3
    return largest


# Input numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find and print the largest number
largest_number = find_largest(num1, num2, num3)
print(f"The largest number is: {largest_number}")

name=input("Enter")