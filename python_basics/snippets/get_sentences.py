# we create a list into which we can put the sentences we define
nulines =  []
for ix,z in enumerate(lines):
    # we remove the final newline character
    line = z.strip()
    print(f"\nRaw line {ix}: {line}")
    # we split off the punctuation marks that do not trigger sentence breaks
    line = re.sub("([a-zA-Zäöü])([;,])","\\1 \\2",line)
    # for puncuation marks that should result in sentencce breaks we do two things:
    # we separate them from their preceding letter AND we add a newline character [as a marker] after the puncutation mark
    line = re.sub("([a-zA-Zäöü])([\.\!\?,])","\\1 \\2\n",line)
    print(f"\nreformated line {ix} <<{line}>>")
    # now that we have newline characters, we can split the text of a line into sentences based on them
    sublines = re.split("\n",line)
    nulines.extend(sublines)
print("\nReformated sentences")
for nl in nulines:
    print(f"|{nl}|")
