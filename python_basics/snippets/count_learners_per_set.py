# Option A
# wir zählen wie oft die beiden set ids 1 und 2 in der Spalte "set" vorkommen.
print(df["set"].value_counts())

# Option B
# wir haben schon gesehen, dass wir mit len() die Zeilen eines Dataframes bestimmen können.
# Den Datenframe für set1 haben wir oben schon erzeugt.
print(len(set1_df))
set2_df = df[df["set"] == 2]
print(len(set2_df ))
