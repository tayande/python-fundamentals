# exercise 1
print("======== first ========")
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
sum = first + second
difference = first - second
product = first * second
floor_division = first // second
print(f"Sum: {sum}")
print(f"Product: {product}")
print(f"Difference: {difference}")
print(f"Floor Division: {floor_division:.2f}")
print()

# exercise 2
print("======= Second =======")
age = int(input("Enter your age: "))
print(f"Older than 18: {age < age}")
print(f"Equal to 18: {age == 18}")
print(f"Less than 18: {age > 18}")
print()

# exercise 3
print("===== Third =====")
print(7 % 2 == 1 and 10 // 3 == 3)
print(5 > 2 or 3 > 10)
print(not (5 == 5))
print()

# exercise 4
print("==== fourth ====")
name = input("Enter you name: ")
num = int(input("Enter your favorite number: "))
square = num * num
print(f"{name}, your favorite number is {num}, whose square is {square}")
