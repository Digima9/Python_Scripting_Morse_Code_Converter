from converter import Converter


word = input("please enter a word : ").upper()
converter = Converter(word)
print(f"Morse converted word is : {converter.encrypted}")

decrypt = input("would you like to decrypt Y/N : ").upper()

if decrypt == "Y":
    print(f"decrypted word is : {converter.decrypt}")



