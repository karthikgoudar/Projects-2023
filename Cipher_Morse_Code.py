'''
Author: Karthik Goudar
date  :  17 JAN, 2023
'''
 
Morse_Code_Dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.",
    "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
    "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
    "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
    "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.", "0": "-----", "&": ".-...", "@": ".--.-.",
    ":": "---...", ",": "--..--", ".": ".-.-.-", "'": ".----.", '"': ".-..-.",
    "?": "..--..", "/": "-..-.", "=": "-...-", "+": ".-.-.", "-": "-....-",
    "(": "-.--.", ")": "-.--.-", "!": "-.-.--", " ": "/"
}

Reverse_Dict = {value:key for key, value in Morse_Code_Dict.items()}


def encrypt(message: str) -> str:
    """
    >>> encrypt("Sos!")
    '... --- ... -.-.--'
    >>> encrypt("SOS!") == encrypt("sos!")
    True
    """
    return " ".join(Morse_Code_Dict[char] for char in message.upper())


def decrypt(message: str) -> str:
    """
    >>> decrypt('... --- ... -.-.--')
    'SOS!'
    """
    return "".join(Reverse_Dict[char] for char in message.split())


def main() -> None:
    """
    >>> s = "".join(Morse_Code_Dict)
    >>> decrypt(encrypt(s)) == s
    True
    """ 
    message = "Save Our Soul!"
    print(message)
    message = encrypt(message)
    print(message)
    message = decrypt(message)
    print(message)


if __name__ == "__main__":
    main()
