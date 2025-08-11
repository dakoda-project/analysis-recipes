# Vokale definieren
vowels = 'aeiouäöü'
# Zählvariable
vowelCount = 0
# Wort definieren
word = 'Oberbürgermeisterin'

# wir transformieren den String von einer Liste von Buchstaben zu einer Menge, um die sich wiederholenden Buchstaben loszuwerden
for letter in set(word.lower()):
    if letter in vowels:
        vowelCount = vowelCount + 1 # add 1
print(vowelCount)
