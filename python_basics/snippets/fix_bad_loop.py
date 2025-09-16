word = 'Oida'
vowels = 'aeiou'
position = 0
consonants = 0
while position < len(word):
    letter = word.lower()[position]
    if letter not in vowels:
        consonants +=1
        print(letter)
    position += 1
print(f"found {consonants} consonants")
