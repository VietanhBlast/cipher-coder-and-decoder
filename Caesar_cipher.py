import string

plain_text = input("Enter the text you want to encrypt: ")
shift = int(input("Enter a number to shift by: "))
shift %= 26

alphabet = string.ascii_letters
shift = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet,shift)

encrypted = plain_text.translate(table)

print(plain_text)
print(encrypted)

