student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
print(nato_data_frame)
nato_dict = {row.letter:row.code for (index,row) in nato_data_frame.iterrows()}
print(nato_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter your name to get your nato phonetic code : ")
# user_nato = [nato_dict. for word in user_input if word in nato_dict.items()]

# user_nato = []
# for word in user_input:
#     temp = nato_dict.get(word.capitalize())
#     user_nato.append(temp) 
user_nato = [nato_dict.get(word.capitalize()) for word in user_input]   
print(user_nato)
