def caesar_cipher(text, key):
    """
    Encrypted the given plaintext with the key provided by the user.

    Args:
        text: plaintext message provided by the user.
        key: number of positions to shift the letters by.
    Returns:
        Encrypted message
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    shifted_alphabet = alphabet[key: ] + alphabet[:key]

    ciphertext = ''
    for char in text:
        if char.isalpha(): # Checking if the character is an alphabet. The cipher doesn't do numbers
            ciphertext += shifted_alphabet[alphabet.index(char)]
        else:
            ciphertext += char

    return ciphertext

if __name__ == "__main__":
    print("Ceasar Cypher Generator")
    plaintext = input("Enter the text you want to encrypt: ")
    key = int(input("Enter the number of positions you want to shift by:"))
    encrypted_msg = caesar_cipher(plaintext, key)
    print(f"The encrypted message is: {encrypted_msg}")


