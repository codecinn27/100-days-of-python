#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        
invitation_list = []
with open("Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()
    print(names)
    
with open("Input/Letters/starting_letter.txt") as file:
    letter = file.readlines(100)
    print(letter)
    
for x in names:
    letter_temp = letter.copy()
    letter_temp[0] = letter_temp[0].replace("[name]",x)
    print(x)
    print(letter_temp)
    with open(f"Output/ReadyToSend/{x}.txt", mode="w") as file:
        content = ''.join(letter_temp)
        file.write(content)
    
    


    

