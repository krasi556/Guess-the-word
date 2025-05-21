type = input('Type:\nanimals, celebrities\n')
animals = [
    ["mammals", [["bunny"], ["tiger"], ["cat"], ["dog"]]],
    ["birds", [["sparrow"], ["eagle"], ["parrot"], ["penguin"]]],
    ["reptiles", [["lizard"], ["snake"], ["turtle"], ["crocodile"]]],
    ["amphibians", [["frog"], ["salamander"], ["newt"]]],
    ["fish", [["goldfish"], ["shark"], ["salmon"], ["tuna"]]],
]

celebrities = [["actor", [["leonardo"], ["denzel"], ["meryl"], ["eminem"], ["drake"], ["emma"]]]]
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
import emoji

secret_found = False
if type == 'animals':
    animal_type = input('What classification is the animal: mammals, birds, reptiles, amphibians, fish\n')
    
    for category in animals:
        if category[0] == animal_type:
            secret = random.choice(category[1])[0]
            word_split = list(secret)
            break
elif type == 'celebrities':
    celebrity_type = input('What type of celebrity: actor, singer, etc.\n')
    
    for category in celebrities:
        if category[0] == celebrity_type:
            secret = random.choice(category[1])[0]
            word_split = list(secret)
            break
print('the word has ' + str(len(secret)) + ' letters')
print()
while True:
    letter_not_found = False
    letter = input('\nTry a letter:\n')
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
        help = input('Do you want a letter to be revealed?\nyes / no')
        if help == 'yes':
            if word_found:
                for ch in secret:
                    if ch not in word_found:
                        randomized_letter.append(ch)
                if randomized_letter:
                    new_letter = random.choice(randomized_letter)
                    word_found.append(new_letter)
            else:
                word_found.append(secret[0])
    for j in secret:
        if j in word_found:
            secret_word_ += j
    if secret == secret_word_:
        emoji_output = animals_emoji.get(secret)
        print(f'The secret word is: {secret}')
        
        secret_found = True
        break
    for i in secret:
        if i in word_found:
            element_stored += i
        else:
            element_stored += '_'
    print(f'The word is with lenght: {element_stored}')
