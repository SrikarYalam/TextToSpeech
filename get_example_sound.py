import random

eng_file = open('MIT_wordlist')
ipa_file = open('PossibleSounds_MIT')

num_letters = 0
included_letters = []
letters_map = {}
letters_ipa_map = {}

eng_arr = eng_file.read().split('\n')
ipa_arr = ipa_file.read().split('\n')
for i, word in enumerate(ipa_arr):
    for letter in word:
        if letter not in included_letters:
            num_letters += 1
            included_letters.append(letter)
            letters_map[letter] = [eng_arr[i]]
            letters_ipa_map[letter] = [ipa_arr[i]]
        else:
            letters_map[letter].append(eng_arr[i])
            letters_ipa_map[letter].append(ipa_arr[i])

print('What would you like to do?')
print(f'There are {num_letters} ipa letters in the file:')
print(included_letters)

print()
print('unicode for each character printing...')
for letter in included_letters:
    print(f'{letter} : {ord(letter)}')
    
print()

user_letter = input("Enter a letter to get the words which use the letter: ")
user_nums = input(f'This letter has {len(letters_map[user_letter])} occurances, enter space seperated occurance you would like (r for random 10):\n\t')
print()

if user_nums == 'r':
    user_nums = ""
    for i in range(10):
        user_nums += str(random.randrange(1,len(letters_map[user_letter]))) + " "
for n in user_nums.split():
    num = int(n)
    print(f'word {letters_map[user_letter][num-1]} is pronounced {letters_ipa_map[user_letter][num-1]}')



