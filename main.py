#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open(r".\Input\Names\invited_names.txt", mode="r") as name_file:
    name_list = name_file.readlines()
with open(r".\Input\Letters\starting_letter.txt", mode="r") as letter_file:
    letter_text = letter_file.read()


for name in name_list:
    clear_name = name.strip("\n")
    with open(fr".\Output\ReadyToSend\{clear_name}_invitation.txt", mode="w") as letter_file:
        letter_file.write(letter_text.replace("[name]",clear_name))
