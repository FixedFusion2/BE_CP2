#TE 2nd Morse Code Translator
#List for alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#List for morse code
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
#Menu Function
def menu():
    while True:
        #Print 1. Translate for Morse Code to English
        print("1. Translate for Morse Code to English")
        #Print 2. Translate for English to Morse Code
        print("2. Translate for English to Morse Code")
        #Print 3. View Morse Code
        print("3. View Morse Code Alphabet")
        #View Morse Code Alphabet
        print("4. Exit")
        #Option is set to an input asking for the user to choose an option, 1-3.
        option = input("Choose an option (1-4): ")
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
                for i in range(len(alphabet)):
                    print(f"{alphabet[i].upper()} = {morse_code[i]}")
                go_back = input('Would you like to go back to the menu? (yes/no): ').lower()
                if go_back == "yes":
                    menu()
            case "4":
                print("Exiting...")
                exit()
            #If user selects an invalid option
            case _:
                print("Invalid option. Please try again.")

#Morse to English function
def morse_to_english():
    #While loop for user input
    while True:
        #Morse input is set to an input telling the user to enter the morse code
        morse_input = input("Enter Morse code or 'back' to return to the menu: ")
        #If morse_input is "back"
        if morse_input.lower() == "back":
            #Break loop
            break
        #English_output is set to an empty string
        english_output = ""
        #Split words by " / "
        words = morse_input.split(" / ")
        #For loop for code in morse_list
        for word in words:
            #Letters is set to word split by spaces
            letters = word.split(" ")
            for code in letters:
                #If code is empty
                if code == "":
                    continue
                #If code is in morse_code
                elif code in morse_code:
                    #English output is added to the output string
                    english_output += alphabet[morse_code.index(code)]
                else:
                #If invalid output
                    english_output += "?"
            english_output += " "
        #Print English output
        print("English translation:", english_output)
# English to Morse
def english_to_morse():
    #While loop for user input
    while True:
        #English input is set to an input telling the user to enter the English text
        english_input = input("Enter English text or 'back' to return to the menu: ").lower()
        #If english_input is "back"
        if english_input.lower() == "back":
            break
        #Morse_output is set to an empty string
        morse_output = ""
        #For loop for char in english_input
        for i in range(len(english_input)):
            #Char is set to english_input at index i
            char = english_input[i]
            #If char is a space
            if char == " ":
                #If not morse_output ends with " / "
                if not morse_output.endswith(" / "):
                    #Morse output is added to the output string with a space for words
                    morse_output += " / "
                #Elif Char is in alphabet
            elif char in alphabet:                                                                                                          
                #Morse output is added to the output string without giving errors for spaces
                morse_output += morse_code[alphabet.index(char)] + " "
            else:
                morse_output += "?"

        #Print Morse output
        print("Morse code translation:", morse_output.strip())
#Start the program by calling the menu function
menu()