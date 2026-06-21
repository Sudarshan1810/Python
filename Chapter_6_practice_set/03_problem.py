#A spam comment is defined as a text containing following keywords : "make a lot of money", "buy now", "subsscribe this","click this"
#write a porogram to detect these spams 

p1="Make a lot of money"
p2="Click this"
p3="subscribe this"
p4="buy now"

comment = input("Type your comment here: ")

if(p1 in comment or p2 in comment or p3 in comment or p4 in comment):
     print("This is a spam comment")

else:
     print("Thankyou! for commenting")
