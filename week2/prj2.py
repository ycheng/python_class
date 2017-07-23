# version 3

ar = [3, 78, 42, 23, 66, 9]
n = len(ar)

print(ar)

for i in range(n):
    for j in range(i+1, n):
       if ar[i] > ar[j]:
          (ar[i], ar[j]) = (ar[j], ar[i])

print(ar)
