first = input("Enter first number: ")
second = input("Enter second number: ")
third = input("Enter third number: ")

count = 0

if first == second and first == third:
    count = 3
elif first == second or first == third or second == third:
    count = 2

print(count)