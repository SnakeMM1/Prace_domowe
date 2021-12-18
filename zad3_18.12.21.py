#%%
# Napisz funkcje ktora zwroci liczbe obiektow typu str o dlugosci powyzej dwoch znakow w obiekcie iterowanym (lista, tupla)


Lista = [(7, 8, 89), (5, 7), (4, 4), (9, 5, 6, 2), (7, 8, 4, 5, 6), (4, 5, 7)]

Lista1=['art', '987', 'iu', 'op', '986', 'kol', '88', '5yt', '99999']


def Ile(X):
    d = 0
    for i in X:
        if len(i) > 2:
            d+=1
        else:pass
    print(d)        
Ile(Lista1)
Ile(Lista)





