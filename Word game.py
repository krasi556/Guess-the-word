type = input('Type:\nanimals, celebrities\n').lower()
animals = [
    ["mammals", [["bunny"], ["tiger"], ["cat"], ["dog"]]],
    ["birds", [["sparrow"], ["eagle"], ["parrot"], ["penguin"]]],
    ["reptiles", [["lizard"], ["snake"], ["turtle"], ["crocodile"]]],
    ["amphibians", [["frog"], ["salamander"], ["newt"]]],
    ["fish", [["goldfish"], ["shark"], ["salmon"], ["tuna"]]],
]
celebrities_gender = {'leonardo':'👨','denzel':'👨','eminem':'👨','meryl':'👩','drake':'👨','emma':'👩'}
celebrities = [["actor", [["leonardo"], ["denzel"], ["meryl"], ["eminem"], ["drake"], ["emma"], ["brad"], ["scarlett"],
                          ["julia"], ["tom"], ["angelina"], ["johnny"]]],
               ["singer", [["beyonce"], ["taylor"], ["adele"], ["rihanna"], ["bruno"], ["justin"], ["weeknd"],
                           ["ariana"], ["ed"], ["shakira"]]]]

animals_emoji = {'bunny': '🐰',
                 'tiger': '🐯',
                 'cat': '🐱',
                 'dog': '🐶',
                 'sparrow': '🐦',
                 'eagle': '🦅',
                 'parrot': '🦜',
                 'lizard': '🦎',
                 'snake': '🐍',
                 'turtle': '🐢',
                 'crocodile': '🐊',
                 'frog': '🐸',
                 'salamander': '🦎',
                 'newt': '🦎',
                 'goldfish': '🐟',
                 'shark': '🦈',
                 'salmon': '🐟',
                 'tuna': '🐟', }
word_found = []
randomized_letter = []
import random
import string
secret_found = False
if type == 'animals':
    animal_type = input('What classification is the animal: mammals, birds, reptiles, amphibians, fish\n')
    valid_outcome = []
    for i in (animals):
        valid_outcome.append(i[0])
    if animal_type not in valid_outcome:
        print('Invalid classification')
        exit()
    for category in animals:
        if category[0] == animal_type:
            secret = random.choice(category[1])[0]
            word_split = list(secret)
            break
elif type == 'celebrities':
    celebrity_type = input('What type of celebrity: actor or singer.\n').lower()
    valid_outcome = []
    for i in (celebrities):
        valid_outcome.append(i[0])
    if celebrity_type not in valid_outcome:
        print('Invalid classification')
        exit()
    for category in celebrities:
        if category[0] == celebrity_type:
            secret = random.choice(category[1])[0]
            word_split = list(secret)
            break
else:
    print('Invalid type')
    exit()
print('the word has ' + str(len(secret)) + ' letters')
print()

while True:
    letter_not_found = False
    letter = input('\nTry a letter:\n').lower()
    if not letter.isalpha():
        print('Please enter a letter!')
        continue
    if letter in word_found:
        print('It\'s already revealed!')
        continue
    if len(letter) == 1 and letter.isalpha():
        if letter in secret:
            if letter not in word_found:
                word_found.append(letter)
        else:
            letter_not_found = True
    else:
        print('Invalid input. Please enter a single letter.')
        continue
    secret_word_ = ''
    element_stored = ''
    if letter_not_found:
        print(f'There\'s no "{letter}" there')
        help = input('Do you want a letter to be revealed?\nyes / no\n').lower()
        if help == 'yes':
                for ch in secret:
                    if ch not in word_found:
                        randomized_letter.append(ch)
                if randomized_letter:
                    for i in randomized_letter:
                        if i not in word_found:
                            word_found.append(i)
                            break
                else:
                    word_found.append(secret[0])
    for i in secret:
        if i in word_found:
            element_stored += i
        else:
            element_stored += '_'
    if secret == element_stored:
        emoji_output = ''
        if type == 'animals':
            emoji_output = animals_emoji.get(secret)
        elif type == 'celebrities':
            emoji_output = celebrities_gender.get(secret)
        print(f'The secret word is:  \033[32m{secret}\033[0m{emoji_output}')
        secret_found = True
        break
    if not secret_found:
        print(f'The word is with length: {element_stored}')