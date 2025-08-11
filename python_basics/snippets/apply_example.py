# Stärker komprimierte Variante

df["Proficiency Min"] = df["Proficiency level"].apply(lambda x: x.split("/")[0] if "/" in x else x)
df["Proficiency Max"] = df["Proficiency level"].apply(lambda x: x.split("/")[1] if "/" in x else x)
print(df.tail())
