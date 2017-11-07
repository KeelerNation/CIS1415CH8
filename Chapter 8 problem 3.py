def encrypt_sentence():
    global codes
    codes = {'A': '@', 'a': '9', 'B': '%', 'b': '#', 'C': '$', 'c': '4', 'D': '5', 'd': '6', 'E': '^', 'e': '6',
             'F': '&', 'f': '7', 'G': '*', 'g': '8', 'H': '(', 'h': '9', 'I': '_', 'i': '-', 'J': '~', 'j': '`',
             'K': ',', 'k': '<', 'L': '.', 'l': '>', 'M': '/', 'm': '?', 'N': ':', 'n': ';', 'O': '{', 'o': '}',
             'P': '[', 'p': ']', 'Q': 'W', 'q': 'w', 'R': 'T', 'r': 't', 'S': 'D', 's': 'd', 'T': 'Y', 't': 'y',
             'U': 'I', 'u': 'i', 'V': 'B', 'v': 'b', 'W': 'E', 'w': 'e', 'X': 'C', 'x': 'c', 'Y': 'U', 'y': 'u',
             'Z': 'X', 'z': 'x', ' ': '__', '.': '.'}

    sentence = input('Enter a sentence or two:\n')
    global decrypted_sentence
    decrypted_sentence = sentence

    word = sentence.split(' ')

    print('Encrypted version: ',end='')
    for letter in word:
        for character in letter:
            if character in codes:
                print(codes[character], end='')
    return

def decrypted_text():
    print('Decrypted version:',decrypted_sentence)

    return
encrypt_sentence()
print('')
decrypted_text()







