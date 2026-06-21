#write a program to calculate the grades of the students from their marks form the following scheme:

# 100-90 => outstanding
# 89-80 => A
# 79-70 => B
# 69-60 => C 
# 59-50 => D 
# <49 => Fail

marks= int(input("Enter your marks: "))

if(100>marks>90 ):
     print("Outstanding")

elif(89>marks>80):
     print("A")

elif(79>marks>70):
     print("B")

elif(69>marks>60):
     print("C")

elif(59>marks>50):
     print("D")

else:
     print("Fail")
