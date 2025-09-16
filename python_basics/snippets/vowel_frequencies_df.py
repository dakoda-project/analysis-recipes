# convert the dictionary vowel_frequencies to a data frame with columns "vowel" and "frequency"
print(vowel_frequencies)
row_list = []
for vowel, freq in vowel_frequencies.items():
    row_dict = {"vowel": vowel, "frequency": freq}
    row_list.append(row_dict)
vowel_df = pd.DataFrame(row_list)
print(vowel_df.head())
