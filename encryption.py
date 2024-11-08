def encrypt(text, key):
    # Ensure the key is exactly 18 digits
    if len(key) != 18 or not key.isdigit():
        raise ValueError("Key must be an 18-digit number.")

    encrypted_text = []
    key_length = len(key)

    for i, char in enumerate(text):
        shift = int(key[i % key_length])

        if char.islower():  # Encrypt lowercase letters
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            encrypted_text.append(shifted_char)
        elif char.isupper():  # Encrypt uppercase letters
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text.append(shifted_char)
        elif char.isdigit():  # Encrypt digits
            shifted_char = chr(((ord(char) - ord('0') + shift) % 10) + ord('0'))
            encrypted_text.append(shifted_char)
        else:
            # Leave special characters unchanged
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def decrypt(encrypted_text, key):
    # Ensure the key is exactly 18 digits
    if len(key) != 18 or not key.isdigit():
        raise ValueError("Key must be an 18-digit number.")

    decrypted_text = []
    key_length = len(key)

    for i, char in enumerate(encrypted_text):
        shift = int(key[i % key_length])

        if char.islower():  # Decrypt lowercase letters
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text.append(shifted_char)
        elif char.isupper():  # Decrypt uppercase letters
            shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text.append(shifted_char)
        elif char.isdigit():  # Decrypt digits
            shifted_char = chr(((ord(char) - ord('0') - shift) % 10) + ord('0'))
            decrypted_text.append(shifted_char)
        else:
            # Leave special characters unchanged
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# Example usage
text = "FileName123"
key = "123456781234567890"
encrypted_text = encrypt(text, key)
print("Encrypted text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted text:", decrypted_text)
