# 1
list = [1, 2, 3, 4, 5]
#And a for loop:

for i in range(len(list)-1):
   if list[i] > 3:
      list.clear()
      list.append(1)
print(list)