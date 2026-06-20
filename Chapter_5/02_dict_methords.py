marks = {
     "Math": 90,
     "Science": 85,
     "English": 92
}

# print(marks.items())  # returns a list of tuples containing key-value pairs
# print(marks.keys())   # returns a list of all keys in the dictionary
# print(marks.values()) # returns a list of all values in the dictionary
# marks.update({"History": 78, "Geography": 82}) # adds a new key-value pair to the dictionary
# print(marks)

print(marks.get("Maths")) # returns None if the key is not found