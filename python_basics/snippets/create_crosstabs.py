crosstab_min = pd.crosstab(df["Proficiency Min"], df["set"])
crosstab_max = pd.crosstab(df["Proficiency Max"], df["set"])

print(crosstab_min)
print(crosstab_max)
