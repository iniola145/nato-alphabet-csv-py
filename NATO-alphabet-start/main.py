# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(alphabet)
new_dict = {row.letter: row.code for (index, row) in alphabet.iterrows()}
print(new_dict)
# for (indexes, rows) in alphabet.iterrows():


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
for i in word:
    print(f"{i}: {new_dict[i]}")
word_list = [new_dict[i] for i in word]
print(word_list)
