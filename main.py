MORSE_CODE = {
                'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '0': '-----',
                '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.',
                 ' ' : '_', '?' : '..--..', '!' : '-.-.--',
                 '.' : '.-.-.-', ',' : '--..--',';' : '-.-.-.',
                 ':' : '---...', '+' : '.-.-.' , '-' : '-....-',
                 '/' : '-..-.' , '=' : '-...-'
            }

def encode_morse(text):
    text = text.upper()
    encoded_text = ""
    for char in text:
        if char == " ":
            encoded_text += "  "
        else:
            encoded_text += MORSE_CODE[char] + " "

    return encoded_text

def decode_morse(message):
    decoded_message = ""
    message = message.replace('   '," _ ")
    morse_code_list = message.split(' ')
    for code in morse_code_list:
        for letter, morse_code in MORSE_CODE.items():
            if code == morse_code:
                decoded_message += letter.lower()
    return decoded_message

print("1. To encode into morse code:")
print("2. To decode into int english:")
n = int(input("enter your choice: "))

str_1 = input("Enter the message : ")

if(n == 1):
    print(encode_morse(str_1))
else:
    print(decode_morse(str_1.strip()))
