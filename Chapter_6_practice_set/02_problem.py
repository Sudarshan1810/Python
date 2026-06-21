#Write a program to find out weather a student has passed or failed if it requires a total of 40% and atleast 33% in each subject and take marks as an input from the user

science = int(input("Enter your marks you scored in science: "))
maths = int(input("Enter your marks you scored in maths: "))
hindi = int(input("Enter your marks you scored in hindi: "))

percentage = float((science + maths + hindi)/300 *100)

print("You Scored " + str(percentage) + "%")

if(percentage >= 40 and science>=33 and maths>=33 and hindi>=33 ):
     print("You have sucessfully Passed the exam")

else:
     print("You Failed the exam, Try again Next Year!")
