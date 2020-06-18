from collections import Counter


text = input("Enter the text: \n")


c = dict(Counter(text))


number_of_odds = 0


for i in c.values():
    if i%2 != 0:
        number_of_odds += 1



if number_of_odds > 1:
    print("Not a palindrom")
else:
    print("its palindrom permutation")



