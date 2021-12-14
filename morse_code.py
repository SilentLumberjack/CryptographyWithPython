MORSE_SIGNS_DICT = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....",
                    "I": "..", "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
                    "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
                    "Y": "-.--", "Z": "--..", "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
                    "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", " ": "/"}


def encrypt_message(msg):
    encrypted_message = ""
    for letter in msg:
        encrypted_message += MORSE_SIGNS_DICT[letter.upper()] + " "
    return encrypted_message


def decrypt_message(msg):
    decrypted_message = ""
    coded_signs_list = msg.split()
    key_list = list(MORSE_SIGNS_DICT.keys())
    values_list = list(MORSE_SIGNS_DICT.values())
    for coded_signs in coded_signs_list:
        position = values_list.index(coded_signs)
        decrypted_message += key_list[position]
    return decrypted_message


while True:
    process_option = input(
        "1 - encrypt message\t\t2 - decrypt code\t3 - exit\nEnter a process that you want to perform: ")

    if process_option == "1":
        msg_to_encrypt = input("Enter a message to be encrypted with Morse code: ")
        try:
            encrypted_msg = encrypt_message(msg_to_encrypt)
            print("Your encrypted message is: {msg}".format(msg=encrypted_msg))
        except KeyError:
            print("Please, use only English alphabet and roman numbers.")
    elif process_option == "2":
        msg_to_decrypt = input("Enter a message to be decrypted from Morse code: ")
        try:
            decrypted_msg = decrypt_message(msg_to_decrypt)
            print("Your decrypted message is: {msg}".format(msg=decrypted_msg.lower()))
        except ValueError:
            print("You encrypted message contains invalid Morse symbols.")
    elif process_option == "3":
        print("Bye!")
        break
    else:
        print("Unsupported operation type.")
