#write a program which finds out wheather a given name is present in a list or not

I = ["Ramesh", "Suresh", "Mukesh", "Rohit"]

name = input("Enter your name here: ")

if(name in I):
     print("Your name is in the list")
else:
     print("Your name is not in the list")