df["Proficiency Min"]=""
df["Proficiency Max"]=""
for ix, row in df.iterrows():
	if re.search("/" , row["Proficiency level"]):
		df.loc[ix, "Proficiency Min"] = re.split("\/",row["Proficiency level"])[0]
		df.loc[ix, "Proficiency Max"] = re.split("\/",row["Proficiency level"])[1]
	else:
		df.loc[ix, "Proficiency Min"] = row["Proficiency level"]
		df.loc[ix, "Proficiency Max"] = row["Proficiency level"]
print(df.tail())

