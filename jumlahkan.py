a = input().split()
for i in range(len(a)):
    a[i] = int(a[i])
jumlah = 0
for i in range(len(a)):
    jumlah += a[i]
print(jumlah)
