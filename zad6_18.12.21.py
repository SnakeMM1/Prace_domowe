#%%
#Dane sa dwie listy o jednakowej dlugosci. Wykorzystaj funkcje map() oraz wyrazenie lambda i przeksztalc je w jedna ktora zawiera reszte z dzielenia odpowiedniego elementu pierwszej listy przez druga.

numbers1 = [5, 6, 3, 2, 11]
numbers2 = [7, 9, 3, 3, 7]

wynik = map(lambda x,y: x % y, numbers1, numbers2)

print(list(wynik))