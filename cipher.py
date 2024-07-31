message = input("insert message you wish to encrypt: ")
key = input("insert word to act as key: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

def encryptor(message, key):
    encrypted = ""
    passcode = 0

    for x in key.lower():
        coded = alphabet.find(x)
        passcode += coded

    for x in message:
        if x.lower() in alphabet:
            finder = alphabet.find(x.lower())
            letter = alphabet[(finder + passcode ) % 26]
            encrypted += letter

    return encrypted

def decryptor(encrypted, key):
    decrypted = ""
    passcode = 0

    for x in key.lower():
        coded = alphabet.find(x)
        passcode += coded

    for x in encrypted:
        if x.lower() in alphabet:
            finder = alphabet.find(x.lower())
            letter = alphabet[(finder + passcode * -1) % 26]
            decrypted += letter


    return decrypted

encrypted_message = encryptor(message, key)
print(f"Encrypted message: {encrypted_message}")
decrypted_message = decryptor(encrypted_message, key)
print(f"Decrypted message: {decrypted_message}")