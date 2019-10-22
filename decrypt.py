n = input().split()
a = input().split()
no = []
for i in range(len(n)):
    n[i] = int(n[i])
for i in range(len(a)):
    a[i] = int(a[i])
jumlah = n[0]
kortk = n[1]

asc_tk = 96
asc_k = 64


if kortk == 1: #tidak kapital
    for i in range(jumlah):
        a[i] = chr(asc_tk+a[i])
        print(a[i], end="")
elif kortk == 0:#kapital
    for i in range(jumlah):
        a[i] = chr(asc_k+a[i])
        print(a[i], end="")
print()

    
