#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

starting_letter_file = open('/Input/Letters/starting_letter.txt', 'r')
names_file = open('/Input/Names/invited_names.txt', 'r')
starting_letter_read_lines = starting_letter_file.readlines()
names = names_file.readlines()
word_to_replace = '[name]'
for name in names:
    name = name.strip()
    file = open(f'/Output/ReadyToSend/{name}.txt', 'w')
    
    for letter_line in starting_letter_read_lines:
        if starting_letter_read_lines.index(letter_line) == 0:
            letter_line = letter_line.replace(word_to_replace, name)

        letter_line = letter_line.strip()
        letter_line = letter_line + '\n'
        
        file.write(letter_line)
    
    file.close()
        