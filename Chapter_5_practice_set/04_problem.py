#What will be the length of the set after the add operation is performed?

s = set()

s.add(20)
s.add(20.0)
s.add("20")
print(s)
A = len(s)
print(A) 

# the length of the set will be 2