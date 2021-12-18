#%%
#Napisz funkcje ktora przyjmie liste slow i zwroci dlugosc najdluzszego z nich
def Find(list):
    for i in list:
        if len(list(i)) > len(list(i+1)):
            pass
        else: pass

def Elem(liczba):
    lst = []
    i = 0
    for i in range (i, liczba):
        n = input(f"podaj {i} element")
        lst.append(n)
    print(lst)
    Find(lst)



Liczba_elem = int(input("Ile elementów chcesz podac?"))
Elem(Liczba_elem)




