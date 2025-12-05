#Question #15: sentence splitter

statement = input("Enter a sentence: ")
arr = statement.split(' ')

freq_dictionary = {}
for i in arr:
    if i in freq_dictionary:
        freq_dictionary[i] += 1
    else:
        freq_dictionary[i] = 1
print(freq_dictionary)
