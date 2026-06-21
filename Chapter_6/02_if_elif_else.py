age=int(input("Enter your age: "))

if(age>=18):
     print("You are eligible to vote")

elif(age==0):
     print("You are entering 0 as your age")

elif(age<0):
     print("Invalid Age")  

else: 
     print("You are not eligible to vote")

print("Thank you for using our service")