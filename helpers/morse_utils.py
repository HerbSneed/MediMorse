MORSE_CODE_DICT = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.",  "(": "-.--.",  ")": "-.--.-",
    "&": ".-...",  ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.",  "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-","@": ".--.-.", " ": "/"
}

def morse_conversion(string):
    """
    Converts a given string into Morse code.

    Parameters:
        string (str): The alert message to convert.

    Returns:
        str: The Morse code translation of the input string,
             with individual Morse letters separated by spaces.
    """
    message = []
    for let in string:
        if let in MORSE_CODE_DICT:
            message.append(MORSE_CODE_DICT[let])
        else:
            continue
    return ' '.join(message)

def reverse_translation(code):
    """
    Converts Morse code into English.

    Parameters:
        code (str): Morse code string, with letters separated by spaces and words separated by '/'.

    Returns:
        none
    """
    reverse_morse_code_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = code.split("/")
    decoded_text = ""
    for word in words:
        # Split by space between letters
        letters = word.split(" ")
        for letter in letters:
            if letter in reverse_morse_code_dict:
                decoded_text += reverse_morse_code_dict[letter]
            else:
                continue
        # Add space between words
        decoded_text += " "
    print(f"Decoded Message: {decoded_text.strip()}")
    input("Press Enter to return to the main menu...")
    return
