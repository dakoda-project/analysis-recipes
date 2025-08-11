from collections import Counter
wort_liste = ["Lösung","haus", "Appell", "ist" ,"Mut", "Armeechef", "zu", ]
stopwords = ["ab", "auf", "zu", "ist", "war", "mit", "bin", "bist", "warst", "waren", "ohne"]
vowels= 'aeiouäöü'
firstvowels=[]

for word in wort_liste:
	# Wenn wir ein Stopwort haben , interessiert uns sein erster Vokal nicht: wir tun gar nichts.
	# Die Inspektion der Buchstaben im else-Zweig wird nicht erreicht.
	if word in stopwords:
		pass
	else:
		for letter in word.lower():
    			if letter in vowels:
    				firstvowels.append(letter)
        	        # da uns nur der erste Vokal interessiert, können wir abbrechen , wenn wir ihn gefunden haben
        	        # Beachte, dass wir nur die Buchstabenschleife verlassen. Wir gehen aber weiter zum nächsten Wort!
    				break
c=Counter(firstvowels)
print(c)
