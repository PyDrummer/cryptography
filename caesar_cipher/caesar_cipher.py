import nltk
nltk.download('words', quiet=True)
from nltk.corpus import words
word_list = words.words()
# print(word_list)

upper_alphabet= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower_alphabet = []
for i in range(len(upper_alphabet)):
    lower_alphabet.append(upper_alphabet[i].lower())
# print(lower_alphabet)

test = "Ravenala"
test2 = 'It was the best of times, it was the worst of times.'
test3 = 'quondamly'
key = 2

def encrypt(entered, key):
    encrypted = ''
    for char in entered:
        if char not in upper_alphabet and char not in lower_alphabet:
            encrypted += char
        elif char in upper_alphabet:
            temp = upper_alphabet.index(char)
            temp2 = (temp + key) % 26
            encrypted += upper_alphabet[temp2]
        else:
            temp = lower_alphabet.index(char)
            temp2 = (temp + key) % 26
            encrypted += lower_alphabet[temp2]
    return encrypted


def decrypt(encoded, key):
    decrypted = encrypt(encoded, -key)
    return decrypted


def crack(encoded):
    # cracked_encryption = {}
    word_count = []
    for i in range(len(upper_alphabet)):
        word = ''
        count = 0
        
        for char in encoded:
            if char in upper_alphabet:
                num = upper_alphabet.index(char)
                num = (num - i) % 26
                word += upper_alphabet[num]
                # print(word)
            elif char in lower_alphabet:
                num = lower_alphabet.index(char)
                num = (num - i) % 26
                word += lower_alphabet[num]
            else:
                word += char

        words = word.split()
        for w in words:
            if w in word_list:
                count += 1
        w_c = [word, count]
        word_count.append(w_c)
    
    value = word_count[0][1]
    counter = 0
    for i in range(len(word_count)):
        if value < word_count[i][1]:
            counter += 1
            # print(counter)
            value = word_count[i][1]

    return word_count[counter][0]

# print(encrypt(test2, key))
decrypt_test = encrypt(test2, key)
# print('decrypt ', decrypt(decrypt_test, key))
print(crack(decrypt_test))