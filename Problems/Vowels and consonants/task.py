user_input = input()
vowel = "aeiou"
consonant = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
             'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']

for letter in user_input:
    if letter.upper() in consonant:
        print("consonant")
    elif letter.lower() in vowel:
        print("vowel")
    else:
        break
