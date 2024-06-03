class Converter:
    def __init__(self, text):
        self.text = text
        self.morse = {'A': '.-', 'B': '-...',
                      'C': '-.-.', 'D': '-..', 'E': '.',
                      'F': '..-.', 'G': '--.', 'H': '....',
                      'I': '..', 'J': '.---', 'K': '-.-',
                      'L': '.-..', 'M': '--', 'N': '-.',
                      'O': '---', 'P': '.--.', 'Q': '--.-',
                      'R': '.-.', 'S': '...', 'T': '-',
                      'U': '..-', 'V': '...-', 'W': '.--',
                      'X': '-..-', 'Y': '-.--', 'Z': '--..',
                      '1': '.----', '2': '..---', '3': '...--',
                      '4': '....-', '5': '.....', '6': '-....',
                      '7': '--...', '8': '---..', '9': '----.',
                      '0': '-----', ', ': '--..--', '.': '.-.-.-',
                      '?': '..--..', '/': '-..-.', '-': '-....-',
                      '(': '-.--.', ')': '-.--.-'}
        self.convert = []

        self.encrypted = self.encrypt(text)
        self.decrypted = ""

    def encrypt(self, text):
        for item in text:
            morse_letter = self.morse[item]
            self.convert.append(morse_letter)

        morse = ''.join(str(i) for i in self.convert)
        return morse

    @property
    def decrypt(self):
        for item in self.convert:
            values = list(self.morse.values())  # making a value list of Morse dictionary
            keys = list(self.morse.keys())  # making a key list of Morse dictionary
            key_index = values.index(item)  # finding the index from values list

            alphabet_letter = keys[key_index] # the index value from the values list will show us decrypted letter
            self.decrypted += alphabet_letter

        return self.decrypted
