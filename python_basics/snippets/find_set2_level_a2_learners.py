set2_ids = df[ df["set"] == 2 ]["ID"].tolist()
a2_ids = df[ df["Proficiency level"] == "A2"]["ID"].tolist()
schnittmenge=set(set2_ids).intersection(set(a2_ids))
print(list(schnittmenge))

# Kompaktere Alternative, die die Funktionalität von pandas nutzt: 
# wir bilden einen neuen Dataframe, in dem wir nur die Zeilen für Set 2 und Proficiency level A2 behalten.
set2_a2_df = df[ (df["set"] == 2) & (df["Proficiency level"] == "A2") ]
print(set2_a2_df["ID"].tolist())

