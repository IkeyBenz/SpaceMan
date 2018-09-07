from wordGenerator import generateRandomWord
from phraseController import SpaceManPhrase

category = 'Art'

print('\n----- SpaceMan -----')
print('\tCategory:', category, '\n')

print('Loading phrase...')
randomPhrase = generateRandomWord(category)
hiddenPhrase = SpaceManPhrase(randomPhrase)

currentLimbs = 0
maxLimbs = 6

stillAlive = currentLimbs < maxLimbs
stillGuessing = stillAlive and not hiddenPhrase.isSameAsGuess()

print('Starting Game...\n')

def getLetterGuess():
    letter = input('Guess a letter: ').lower()
    if not len(letter) == 1:
        print('Your input was the wrong length. Please input one letter.')
        return getLetterGuess()
    elif not 123 > ord(letter) > 96:
        print('Your input was not an english letter.')
        return getLetterGuess()
    elif letter in hiddenPhrase.alreadyGuessed:
        print('You already guessed that letter.')
        return getLetterGuess()
    else:
        return letter

while stillGuessing:
    print('\n-------', 'Limbs Left:',maxLimbs-currentLimbs,'------\n')
    print(hiddenPhrase.displayable())
    letterGuess = getLetterGuess()
    if hiddenPhrase.has(letterGuess):
        print('Nice!')
    else:
        print('Nope!')
        currentLimbs += 1
    
    stillGuessing = currentLimbs < maxLimbs and not hiddenPhrase.isSameAsGuess()
    if stillGuessing:
        print("Previous Guess's:", ', '.join(hiddenPhrase.alreadyGuessed))
    if currentLimbs == maxLimbs: print('Loser!')
    

print('The word was', hiddenPhrase.original)



