# 1
list = [1, 2, 3, 4, 5]
#And a for loop:

for i in range(len(list)-1):
   if list[i] > 3:
      list.clear()
      list.append(1)
print(list)


list_1 = [['a', 'b'], ['a', 'c'], ['a', 'c'], ['a', 'c'], ['b', 'e'], ['d', 'q'], ['d', 'q']]
new_dict={}
new_list=[]
entry = ()
for l in list_1:
    if tuple(l) in new_dict:
        new_dict[tuple(l)] += 1
    else:
        new_dict[tuple(l)] = 1
for key in new_dict:
    entry = list(key)
    entry.append(new_dict[key])
    new_list.append(entry)
print (new_list)