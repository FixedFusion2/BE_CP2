# morseCode.py
# GitHub Copilot

# PSEUDOCODE:
# 1. Define two tuples: ENGLISH (A-Z, 0-9) and MORSE (corresponding codes).
# 2. Create function english_to_morse(text):
#    - Normalize text to uppercase
#    - For each character: map to morse or use '/' for space or '?' for unknown
#    - Join morse tokens with spaces and return
# 3. Create function morse_to_english(code):
#    - Split morse by spaces, treat '/' as word separator
#    - Map each morse token to an english character or '?' for unknown
#    - Return joined English string
# 4. Main loop:
#    - Present menu to user (English->Morse, Morse->English, Exit)
#    - Read input, call appropriate function, show formatted output
#    - Repeat until user chooses Exit

# Tuples of characters and their Morse equivalents (same index order)
ENGLISH = tuple("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

MORSE = (
    ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",    # A-I
    ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.",  # J-R
    "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..",         # S-Z
    "-----", ".----", "..---", "...--", "....-", ".....", "-....",    # 0-6
    "--...", "---..", "----."                                         # 7-9
)

def english_to_morse(text):
    """
    Convert an English string to Morse code.
    Words are separated by ' / ' in Morse output.
    Unknown characters are represented by '?'.
    """
    # Normalize input
    text = text.upper()

    morse_tokens = []
    for ch in text:
        if ch == " ":
            # Use '/' to separate words in Morse output
            morse_tokens.append("/")
        elif ch in ENGLISH:
            idx = ENGLISH.index(ch)
            morse_tokens.append(MORSE[idx])
        else:
            # Basic error handling: represent unknown characters
            morse_tokens.append("?")

    # Use a single space between Morse letters for readability
    return " ".join(morse_tokens)


def morse_to_english(code):
    """
    Convert Morse code into English.
    Expect letters separated by spaces; words can be separated by '/' token.
    Unknown Morse tokens are represented by '?'.
    """
    # Clean up and split on spaces to get tokens
    tokens = code.strip().split()

    english_chars = []
    for token in tokens:
        if token == "/":
            # Word separator -> add a space in English output
            english_chars.append(" ")
        elif token in MORSE:
            idx = MORSE.index(token)
            english_chars.append(ENGLISH[idx])
        else:
            # Basic error handling for unknown Morse symbols
            english_chars.append("?")

    # Join characters; multiple spaces may appear if input had consecutive '/'
    # Normalize consecutive spaces to a single space
    result = "".join(english_chars)
    return " ".join(result.split())


def main():
    # Main user interaction loop
    while True:
        print()
        print("Morse Code Translator")
        print("---------------------")
        print("1) English -> Morse")
        print("2) Morse -> English")
        print("3) Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            text = input("Enter English text to translate: ").rstrip("\n")
            morse = english_to_morse(text)
            # Nicely format output: show input and result
            print("\nEnglish: " + text)
            print("Morse  : " + morse)

        elif choice == "2":
            code = input("Enter Morse code (use spaces between letters and '/' between words): ").rstrip("\n")
            english = morse_to_english(code)
            print("\nMorse  : " + code)
            print("English: " + english)

        elif choice == "3" or choice.lower() in ("exit", "quit", "q"):
            print("Exiting translator. Goodbye.")
            break

        else:
            # Basic error handling for menu selection
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()