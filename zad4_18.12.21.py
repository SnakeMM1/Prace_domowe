from math import factorial

#%%
#Napisz funkcje obliczjaca silnie
x = int(input('Podaj liczbe'))
i = 1
f = 1
while i != x:
    f = f * (i+1)
    i += 1

print(f"Wynik to: {f}")

#%%
def silnia(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
print(silnia(int(input("Podaj liczbe"))))
# %%
def silnia1(n):
    if n > 1:
        return n*silnia1(n-1)
    return 1
        
print(silnia1(int(input("Podaj liczbe"))))

#%%
def silnia2(n):
    s = 1
    for i in range (2, n+1):
        s *= i
    return s
        
print(silnia2(int(input("Podaj liczbe"))))

#%%

def silnia3(n): return n*silnia3(n-1) if n > 1 else 1
print(silnia3(int(input("Podaj liczbe"))))