import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def caesar(shift):
        encrypted_text = ''
        if shift > len(alphabet):
            shift = shift % len(alphabet)

        for letter in text:
            if letter in alphabet:
                if direction == 'encode':
                    encrypted_letter_index = alphabet.index(letter) + shift

                    if encrypted_letter_index >= len(alphabet):
                        encrypted_letter_index = encrypted_letter_index - len(alphabet)
                elif direction == 'decode':
                    encrypted_letter_index = alphabet.index(letter) - shift
                
                encrypted_text += alphabet[encrypted_letter_index]
            else:
                encrypted_text += letter
        print('=========')
        print(encrypted_text)
        print('=========')

    caesar(shift)
    user_restart = input('Restart? \n(y / n)\n')
    restart = user_restart == 'y'