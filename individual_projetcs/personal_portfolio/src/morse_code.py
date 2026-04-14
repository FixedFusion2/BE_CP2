#TE 2nd Morse Code Translator
#List for alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
#List for morse code
morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

def main_menu():
    while True:
        print("1. Translate for Morse Code to English")
        print("2. Translate for English to Morse Code")
        print("3. View Morse Code Alphabet")
        print("4. Exit")
        option = input("Choose an option (1-4): ")
        match option:
            case "1":
                morse_to_english()
            case "2":
                english_to_morse()
            case "3":
                for i in range(len(alphabet)):
                    print(f"{alphabet[i].upper()} = {morse_code[i]}")
                go_back = input('Would you like to go back to the menu? (yes/no): ').lower()
                if go_back == "yes":
                    main_menu()  # ← Fixed: was menu(), which doesn't exist
            case "4":
                print("Exiting...")
                return  # ← Fixed: was exit(), which kills the whole program including your GUI
            case _:
                print("Invalid option. Please try again.")

def morse_to_english():
    while True:
        morse_input = input("Enter Morse code or 'back' to return to the menu: ")
        if morse_input.lower() == "back":
            break
        english_output = ""
        words = morse_input.split(" / ")
        for word in words:
            letters = word.split(" ")
            for code in letters:
                if code == "":
                    continue
                elif code in morse_code:
                    english_output += alphabet[morse_code.index(code)]
                else:
                    english_output += "?"
            english_output += " "
        print("English translation:", english_output)

def english_to_morse():
    while True:
        english_input = input("Enter English text or 'back' to return to the menu: ").lower()
        if english_input.lower() == "back":
            break
        morse_output = ""
        for i in range(len(english_input)):
            char = english_input[i]
            if char == " ":
                if not morse_output.endswith(" / "):
                    morse_output += " / "
            elif char in alphabet:
                morse_output += morse_code[alphabet.index(char)] + " "
            else:
                morse_output += "?"
        print("Morse code translation:", morse_output.strip())

if __name__ == "__main__":
    main_menu()