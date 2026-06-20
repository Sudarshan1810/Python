#if the names of 2 friends are same; what will happen to the program in problem 6?

fav_lang = {}
fav_lang["Ramesh"] = "hindi"
fav_lang["Suresh"] = "english"
fav_lang["Mahesh"] = "french"
fav_lang["Ramesh"] = "spanish"

print(fav_lang)


# in case if the names of 2 frineds are same, the value of the first name will be updated with the value of the second name
# the last value assigned to the key will be stored in the dictionary.