

a = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]



print(a)


n = len(a)

rotated = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(a[j][i])

    print(temp)
    print(">>>>>>>>>>>>>>>>>>>>")

    rotated.insert(0, temp)



print(rotated)
print("++++++++++++++++++++++++")
