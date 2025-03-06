print("Ceaser Cipher - Encrypt and Decrypt Your Message")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
user_text = input("Type your message:\n").lower()
user_shift = int(input("Type the shift number:\n"))

def encode(text, shift):
    encoded_text = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_index = letter_index + shift
            if new_index > 25:
                new_index -= 26
            encoded_text += alphabet[new_index]
        else:
            encoded_text += letter
    print(f"The encoded text is {encoded_text}")
    
def decode(text, shift):
    decoded_text = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_index = letter_index - shift
            if new_index < 0:
                new_index += 26
            decoded_text += alphabet[new_index]
        else:
            decoded_text += letter
    print(f"The decoded text is {decoded_text}")
    
if user_choice == "encode":
    encode(user_text, user_shift)
elif user_choice == "decode":
    decode(user_text, user_shift)
else:
    print("Invalid input. Please try again.")