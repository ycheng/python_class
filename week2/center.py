
n = 5
for i in range(n):
  # print(i, 4-i, 1+2*i)
  for j in range(4-i):
    print(" ", end="")
  for j in range(1+2*i):
    print("*", end="")
  print("")

print("***")
print(" *")
print("***")
