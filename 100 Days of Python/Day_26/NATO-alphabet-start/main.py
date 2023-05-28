# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

ABC_data = pandas.read_csv("nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (index,row) in ABC_data.iterrows()}
user_word = input("what name do you want phonetically spelled?").upper()
user_list = [dict[word] for word in user_word]
print(user_list)
