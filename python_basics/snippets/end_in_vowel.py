import re
test_words = ["Kamm", "Pfau", "Heu", "Oma", "Flur","Gebräu"]
vowels = "äöüaeiou"
vokale = ["ä","ö","ü","a","e","i","o", "u"]
for test_word in test_words:
    if test_word[-1].lower() in  vowels: # `vokale` würde hier genauso funktionieren!
        print(f"{test_word} ends in a vowel")
    if re.match("^.*[aeiouäöü]$", test_word.lower()):
        print(f"{test_word} ends in a vowel")
    twl=test_word.lower()
    if twl.endswith("ä")  or twl.endswith("ö") or twl.endswith("ä") or twl.endswith("a")  or twl.endswith("e")  or twl.endswith("i")  or twl.endswith("o") or twl.endswith("u"):
        print(f"{test_word} ends in a vowel")
    
