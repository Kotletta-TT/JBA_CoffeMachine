phone_num = input()

speech_digit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for i in phone_num:
    print(speech_digit[int(i)])