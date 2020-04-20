string1 = input("Enter string1: ")
string2 = input("\n Enter string2: ")


if set(string1) == set(string2):
    print(f"{string1} is permutation of {string2}")
else:
    print("Not a permutation")
