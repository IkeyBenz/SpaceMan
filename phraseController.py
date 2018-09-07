class SpaceManPhrase:
    def __init__(self, phrase):
        self.original = phrase.lower()
        self.alreadyGuessed = []

    def displayable(self):
        return ' '.join([c + ' ' if c in self.alreadyGuessed or c == ' ' else '_ ' for c in self.original])

    def isSameAsGuess(self):
        requiredCharacters = [c for c in self.original if c is not ' ']
        for c in requiredCharacters:
            if c not in self.alreadyGuessed:
                return False
        return True

    def letterAlreadyGuessed(self, letter):
        for c in self.alreadyGuessed:
            if c == letter:
                return True
        return False

    def has(self, letter):
        self.alreadyGuessed.append(letter)
        return letter in self.original