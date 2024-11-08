def encrypt(text, key):
    # Ensure the key is exactly 8 digits
    if len(key) != 18 or not key.isdigit():
        raise ValueError("Key must be an 8-digit number.")

    encrypted_text = []
    key_length = len(key)

    for i, char in enumerate(text):

        if char.isalpha():
            # Get the corresponding key digit (cycle through the key if text is longer than 8)
            shift = int(key[i % key_length])
            
            # Shift the character in UTF-8
            shifted_char = chr(ord(char) + shift)
            
            encrypted_text.append(shifted_char)
        else:
            # If it's a special character, leave it unchanged
            encrypted_text.append(char)

    return ''.join(encrypted_text)

def decrypt(encrypted_text, key):
    # Ensure the key is exactly 8 digits
    if len(key) != 18 or not key.isdigit():
        raise ValueError("Key must be an 8-digit number.")

    decrypted_text = []
    key_length = len(key)

    for i, char in enumerate(encrypted_text):
        if char.isalpha():
            # Get the corresponding key digit (cycle through the key if text is longer than 8)
            shift = int(key[i % key_length])
            
            # Reverse the shift for decryption
            shifted_char = chr(ord(char) - shift)

            # Check for underflow (optional, depending on how you want to handle it)
            if ord(shifted_char) < 0:
                # Wrap around if it goes below valid code points (for demonstration)
                shifted_char = chr(0x10FFFF + ord(shifted_char))

            decrypted_text.append(shifted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# # Example usage
# text = "งานสำคัญ.txt"
# key = "450133451287298068"
# encrypted = encrypt(text, key)
# decrypted = decrypt(encrypted, key)
# print(f"Original text: {text}, Encrypted text: {encrypted}, Decrypted text: {decrypted}")
