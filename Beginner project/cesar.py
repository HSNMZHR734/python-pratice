alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    
    # Reverse the shift for decoding
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)  # wrap around using modulus
            output_text += alphabet[shifted_position]
        else:
            # Keep non-alphabet characters like spaces and punctuation
            output_text += letter

    print(f"\nHere is the {encode_or_decode}d result: {output_text}\n")

# Loop to run program again
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ['encode', 'decode']:
        print("Invalid choice. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Normalize shift to avoid large values
    shift %= 26

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    restart = input("Type 'yes' to go again or 'no' to exit:\n").lower()
    if restart != 'yes':
        print("Goodbye! 👋")
        break
