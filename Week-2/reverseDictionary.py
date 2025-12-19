#Question #16: reversed dictionary

old_dictionary = {"John": "A", "Sara": "B", "Musa": "A"} #demo dictionary
new_dictionary = {}
for i in old_dictionary:
    if old_dictionary[i] in new_dictionary:
        arr = new_dictionary[old_dictionary[i]]
        arr.append(i)
        new_dictionary[old_dictionary[i]] = arr
    else:
        new_dictionary[old_dictionary[i]] = [i]
print(new_dictionary)