
import time

line = 1
while True:
  print("========")
  for i in range(20):
    if i == line:
       print("*")
    else:
       print()
  print("========")
  time.sleep(.8)
  line += 1
  line = line % 20
