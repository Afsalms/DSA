string = input("Enter string to check: ")

if len(string) == len(set(string)):
    print(f"\nAll characters in {string} is unique")
else:
    print(f"\nDuplicate characters in {string}")


