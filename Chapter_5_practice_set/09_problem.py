#Can you change the values inside a list which is contained in a set?
#s = {1, 2, 3, [4, 5]} 

s = {1, 2, 3, [4, 5]} 

#this will give an error because lists are mutable and cannot be added to a set.

s = {1, 2, 3, (4, 5)}

#THIS will work because tuples are immutable and can be added to a set.