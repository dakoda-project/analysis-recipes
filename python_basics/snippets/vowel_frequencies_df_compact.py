# eine weitere noch kompaktere Option
df_vowel_freq = pd.DataFrame.from_records(list(vowel_frequencies.items()),columns=["vowel", "frequency"])
print(df_vowel_freq)


# noch eine  kompakte Option, bei der wir die Vokale als Indizes verwenden statt als WeRte in einer Spalte.
df_vowel_freq = pd.DataFrame.from_dict(vowel_frequencies, orient="index", columns=["frequency"])
print(df_vowel_freq.head())
