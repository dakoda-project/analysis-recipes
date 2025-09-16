# the path to the parse file is as shown below


import os
import re
from collections import Counter
from nltk.util import bigrams

parse_file = "./data/comigs_set_1_bsPg_1_sample.conllu"
if os.path.exists(parse_file):
    print(f"found {parse_file}")

# wir lesen die Datei als Ganzes und erkennen Satzblöcke als von zwei Zeilenumbrüchen getrennte Blöcke
with open(parse_file,"r") as inc:
    file_string=inc.read()
sentences = re.split("\n\n",file_string)
# am Ende der Datei kann eine Folge von zwei Zeilenumbrüchen sein, nach der kein Satz mehr kommt
sentences = [x for x in sentences if not re.match("^\s*$",x)]

sid_2_len={}
upos=[]
vlemmas=[]
letters=[]
toklens= []
token_forms = []
observed_bigrams=[]

for ix,sent in enumerate(sentences):
    # wir zerlegen den Satzblock in eine Liste von Zeilen
    # jede Zeile repräsentiert ein Token
    tokens=re.split("\n",sent)
    del token_forms[:]
    sid_2_len[ix] =len(tokens)
    for tok in tokens:
        # die Infos je Token sind in durch Tabs getrennten Feldern
        fields = re.split("\t",tok)

        form = fields[1].lower()
        token_forms.append(form)
        toklens.append(len(form))
        # Hier könnten wir auch form.lower() verwenden, je nachdem ob wir Klein- und Großbuchstaben unterscheiden wollen
        letters.append(form)
        
        upos.append(fields[4])
        if fields[4].startswith("V"):
          vlemmas.append(fields[2]) 
    # wir ermitteln die Bigramme je Satz!
    observed_bigrams.extend(bigrams(token_forms))


max_len = 0
max_sent_ids=[]
min_len=100000
min_sent_ids=[]
for k,v in sid_2_len.items():
    if v > max_len:
        max_len=v
        del max_sent_ids[:]
        max_sent_ids.append(k)
    elif v==max_len:
        max_sent_ids.append(k)
    else:
        pass

    if v<min_len:
        min_len=v
        del min_sent_ids[:]
        min_sent_ids.append(k)
    elif v== min_len:
        min_sent_ids.append(k)
    else:
        pass
tokencount=sum(sid_2_len.values())
print(f"total tokens {tokencount} in {len(sentences)} sentences")
print(f"Max length {max_len}  in {max_sent_ids}")
print(f"Min length {min_len}  in {min_sent_ids}")


bc=Counter( observed_bigrams)
print("")
print(f"5 häufigste Bigramme: {bc.most_common(5)}")

all_letter_string  = "".join(letters)
letter_counter=Counter(all_letter_string)
print("")
print(f"Buchstabenhäufigkeiten {letter_counter}")
print(f"häufigster Buchstabe: {letter_counter.most_common(1)}")

uposc=Counter(upos)
print("")
print(f"POS-Häufigkeiten {uposc}")

vl_freqs=Counter(vlemmas)
print("")
print("Verblemma Häufigkeiten")
print(vl_freqs)


word_length_counter=Counter(toklens)
descending_word_lengths=sorted(list(word_length_counter.keys()), reverse=True)

print("")
print("Wortlänge\tHäufigkeit")
for wl in descending_word_lengths:
    print(f"{wl}\t{word_length_counter[wl]}")

