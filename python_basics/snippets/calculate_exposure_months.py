def calculate_exposure_months(birth_year, text_creation_year):
	return (text_creation_year - birth_year) * 12


print(calculate_exposure_months(2000,2011))
