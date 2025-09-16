# %load ./snippets/count_bigrams.py
# wir verwenden wieder die Text-Datei aus dem Merlin-Korpus
import re
path_to_file="./data/1091_0000265.txt"
# Die open-Funktion nimmt mehrere Argumente. Das wichtigste ist das erste, der Pfad zur Datei.
with open(path_to_file,"r", encoding='utf-8') as f:
    # mit der Methode readlines lesen wir den Datei-Inhalt in eine Liste von Zeilen.
    lines=f.readlines()
print(lines)

# NB: wir können die obigen Methoden aus re nicht direkt verwenden, weil sie keine überlappenden Treffer zulassen.
# Bei einer Sequenz "Ich mag Eis." wolten wir die Bigramme "Ich mag" , "mag Eis"  und "Eis ." finden und nicht  nur "Ich mag" und "Eis ."

records = {}
all_tokens = []

# Wir erstellen zunächste eine lange Liste von Tokens, in der die Tokens aller Sätze zusammengefügt sind.
for z in lines:
    # we remove the final newline character
    line = z.strip()
    # We separate punctuation marks from preceding alphabetic characters (letters)
    line = re.sub("([a-zA-Zäöü])([\.\!\?,])","\\1 \\2",line)
    # We split the text of the line into a list of tokens
    white_space_tokens = re.split("\s+",line)
    # We join the tokens of all sentences. this means we can get bigrams that cross sentence boundaries!
    all_tokens.extend(white_space_tokens)
ix=0

# Wir ermitteln nun die Bigramme und zählen.
#
# NB: die Einträge in einer Liste beginnen ab Index 0!
#
# ["Ich", "mag" , "Eis" , "." ] Länge 4
# [ 0, 1,2, 3]
# 
# Wir dürfen nicht bis zur letzten Index-Position (3) gehen und dann nach dem Token an Position 3+1 schauen: 
# es gibt nämlich keine Position 4 und wir würden einen Fehler bekommen.
# Der höchste Index ix , den wir besuchen dürfen , ist 2.
# Um das sicherzustellen, testen wir, dass  jeder Index, den wir besuchen,  **kleiner** ist als die Tokenanzahl - 1.
while ix < len(all_tokens)-1:
    bigram = all_tokens[ix]+"_"+all_tokens[ix+1]
    if bigram not in records:
        records[bigram]=0
    records[bigram]+=1
    ix+=1
print(records)
