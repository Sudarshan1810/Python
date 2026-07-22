# Write a program to find wheather the given number is prime or not

num = int(input("Enter a number: "))

for i in range(2, num):
     if num % i == 0:
          print (f"number {num} is not a prime number")
          break
     else:
          print (f"number {num} is a prime number")
          break