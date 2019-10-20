def caesar(text, s):
    cipher = ""
    for char in text:
        if char == ' ':
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + s - 65) % 26 + 65)
        else:
            cipher += chr((ord(char)+s-97) % 26 + 97)

    return cipher


string = input("plain-text: ")
s = int(input("shift: "))
print("original string : ", string)
print("encryption : ", caesar(string, s))
