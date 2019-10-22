a = int(input())
b = input()
if b == "H":
    for i in range(a):
        for j in range(a):
            if i%2 == 0:
                print("#", end="")
            else:
                print("-", end="")
        print()
elif b == "V":
    for i in range(a):
        for j in range(a):
            if j%2 == 0:
                print("#", end="")
            else:
                print("|", end="")
        print()
