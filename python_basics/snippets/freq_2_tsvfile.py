# öffnen Sie eine Datei, in die Sie schreiben können
with open("1091_0000265.freqs.tsv", "w", encoding='utf-8') as out:
    out.write("Token\tHäufigkeit\n")
    for r in sorted_keys:
        out.write(f"{r}\t{freq_records[r]}\n")
