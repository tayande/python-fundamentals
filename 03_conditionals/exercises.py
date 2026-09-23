# exercise 1
print("=== first ===")
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age >= 13 and age <= 19:
    print("Teenager")
else:
    print("Adult")

print()

# exercise 2
print("=== Second ===")
num = int(input("Enter any number: "))
if num < 0:
    print(f"{num} is a Negative number")
elif num == 0:
    print(f"{num} is Zero")
else:
    print(f"{num} is a Positive number")

print()

# exercise 3
print("=== third ===")
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
if first > second and first > third:
    print(f"The highest among the three numbers you provided is {first}")
elif second > first and second > third: 
    print(f"The highest among the three numbers you provided is {second}")
else: 
    print(f"The highest among the three numbers you provided is {third}")

print()

# exercise 4
print("=== Fourth ===")
year = int(input("Enter a year: "))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0 and year % 400 == 0:
        print(f"{year} is a leap year")
    else: 
        print(f"{year} is not a leap year")
else:
    print(f"{year} is not a leap year")       


# exercise 5
x = 15
if x > 10:
    if x > 20:
        print("Big")
    else:
        print("Medium")
else:
    print("Small")