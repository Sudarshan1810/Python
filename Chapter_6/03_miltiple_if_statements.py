age=int(input("Enter your age: "))

#if statement no:1
if(age%2==0):
     print("The age is Even")
#End of if statement no:1

#if statement no:2
if(age>=18):
     print("You are eligible to vote")

elif(age==0):
     print("You are entering 0 as your age")

elif(age<0):
     print("Invalid Age")  

else: 
     print("You are not eligible to vote")
#End of if statement no:2

print("Thank you for using our service")