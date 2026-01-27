#TE 2nd Morse Code Translator
#List for alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
#List for morse code
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","..-","...-",".--","-..-","-.--","--..","/"]
#Menu Function
def menu():
    while True:
        #Print 1. Translate for Morse Code to English
        print("1. Translate for Morse Code to English")
        #Print 2. Translate for English to Morse Code
        print("2. Translate for English to Morse Code")
        #Print 3. Exit
        print("3. Exit")
        #Option is set to an input asking for the user to choose an option, 1-3.
        option = input("Choose an option (1-3): ")
        #Match Option
        match option:
            #If user selects 1 run morse_to_english
            case "1":
                morse_to_english()
            #If user selects 2 run english_to_morse
            case "2":
                english_to_morse()
            #If user selects 3 exit
            case "3":
                print("Exiting...")
                break
            #If user selects an invalid option
            case _:
                print("Invalid option. Please try again.")

#Morse to English function
def morse_to_english():
    #While loop for user input
    while True:
        #Morse input is set to an input telling the user to enter the morse code separated by spaces
        morse_input = input("Enter Morse code (space separated) or 'back' to return to the menu: ")
        #If morse_input is "back"
        if morse_input.lower() == "back":
            #Run menu
            menu()
            #Break loop
            break
        #Morse_list is set to morse_input and split by spaces
        morse_list = morse_input.split(" ")
        #English_output is set to an empty string
        english_output = ""
        #For loop for code in morse_list
        for code in morse_list:
            #If code is in morse_code
            if code in morse_code:
                #English output is added to the output string
                english_output += alphabet[morse_code.index(code)]
            else:
                #If invalid output
                english_output += "?"
        #Print English output
        print("English translation:", english_output)
# English to Morse
def english_to_morse():
    #While loop for user input
    while True:
        #English input is set to an input telling the user to enter the English text
        english_input = input("Enter English text (no spaces) or 'back' to return to the menu: ").lower()
        #If english_input is "back"
        if english_input.lower() == "back":
            #Run menu
            menu()
            #Break loop
            break
        #Morse_output is set to an empty string
        morse_output = ""
        #For loop for char in english_input
        for char in english_input:
            #If char is in alphabet
            if char in alphabet:
                #Morse output is added to the output string
                morse_output += morse_code[alphabet.index(char)] + " "
            else:
                #If invalid output
                morse_output += "?"
        #Print Morse output
        print("Morse code translation:", morse_output)
menu()