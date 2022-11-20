def cipher():
    new_message = []
    message_str = ""
    print("Do you want to decrypt or encrypt a message?")
    cipher_mode = input()
    print("Please input your message: ")
    message = input()
    print("Enter the key number (1-26)")
    key = int(input())
    if cipher_mode.lower() == "encrypt":
        for char in range(len(message)):
            if message[char] == " ":
                new_message.append(" ")
            elif ord(message[char]) >= 65 and ord(message[char]) <= 90:
                char_value = int(ord(message[char]))
                new_char_value = char_value + key
                if new_char_value > 90:
                    new_char_value = (new_char_value - 90) + 64
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
                else:
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
            elif ord(message[char]) >= 97 and ord(message[char]) <= 122:
                char_value = int(ord(message[char]))
                new_char_value = char_value + key
                if new_char_value > 122:
                    new_char_value= new_char_value - 122 + 96
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
                else:
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
            else:
                new_message.append(message[char])
        for i in range(len(new_message)):
            message_str = message_str + new_message[i]
        print(message_str)
    elif cipher_mode.lower() == "decrypt":
        for char in range(len(message)):
            if message[char] == " ":
                new_message.append(" ")
            elif ord(message[char]) >= 65 and ord(message[char]) <= 90:
                char_value = int(ord(message[char]))
                new_char_value = char_value - key
                if new_char_value < 65:
                    new_char_value = 90 - (65 - char_value)
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
                else:
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
            elif ord(message[char]) >= 97 and ord(message[char]) <= 122:
                char_value = int(ord(message[char]))
                new_char_value = char_value - key
                if new_char_value < 97:
                    new_char_value = 121 - (97 - char_value)
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
                else:
                    new_char = chr(new_char_value)
                    new_message.append(new_char)
            else:
                new_message.append(message[char])
        for i in range(len(new_message)):
            message_str = message_str + new_message[i]
        print(message_str)
    else:
        print("There has been an error")
if __name__ == '__main__':
    cipher()
