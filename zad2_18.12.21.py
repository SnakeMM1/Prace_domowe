#%%
# Napisz funkcje ktora sprawdzi czy lista zawiera tylko unikalne wartosci.
#a_list = ["a ", "b ", "c"]

#for index in range(len(a_list)):
#Iterate over numbers used as indices
#    print(a_list[index])

fruits = ['orange', 'apple1', 'pear', 'banana', 'kiwi', 'apple', 'banana']
            
def Check(thelist):
  seen = set()
  for x in thelist:
    if x in seen: return True
    seen.add(x)
    print(seen)
  return False

ans = Check(fruits)
if (ans):
    print("Lista zawiera zdublowane elementy")
else:
    print("Lista jest bez powtarzających się elementow")



#len = len(fruits)


#print(Check(fruits))
#print(list(set([x for x in fruits if fruits.count(x) > 2])))


        