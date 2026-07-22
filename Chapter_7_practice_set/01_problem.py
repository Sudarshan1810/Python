# Write a program to print multiplication table of a given number using for loop

i = int(input("Enter a number to print its multiplication table: "))
for n in range(1, 11):
    print(f"{i} x {n} = {i * n}")
