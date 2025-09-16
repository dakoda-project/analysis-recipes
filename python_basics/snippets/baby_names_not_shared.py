
n2022=set(female_names_2022)
n2024=set(female_names_2024)
shared=n2022.intersection(n2024)
print(f"geteilte Namen {shared}")
only2022=n2022.difference(n2024)
only2024=n2024.difference(n2022)
not_shared = only2022.union(only2024)

print(f"Version A {not_shared}")

# Alternative Lösung mit Listen


def check_names(names1, names2):
    only_names1 = []
    for name in names1:
        if name not in names2:
            only_names1.append(name)
    return only_names1

only2022 = check_names(female_names_2022, female_names_2024)
only2024 = check_names(female_names_2024, female_names_2022)
not_shared =only2022 + only2024
print(f"Version B {not_shared}")
