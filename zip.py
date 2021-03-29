first_coll = [1,2,3,4]
second_coll = [11,12,13,14]
third_coll = list (zip(first_coll,second_coll))
print(third_coll)  #[(1, 11), (2, 12), (3, 13), (4, 14)] зип в список

third_coll = tuple (zip(first_coll,second_coll))
print(third_coll) #((1, 11), (2, 12), (3, 13), (4, 14))   зип в кортеж

third_coll = dict(zip(first_coll,second_coll)) #{1: 11, 2: 12, 3: 13, 4: 14} зип в словарь.
# Работает только при двух итерациях!
print(third_coll)

fourth_coll =  list (zip(third_coll)) # [(1,), (2,), (3,), (4,)]   зип из словаря
print(fourth_coll[1], type(fourth_coll[1]))

third_coll = list (zip(first_coll,second_coll))
fourth_coll = list(zip(third_coll))
print(fourth_coll)
print(*third_coll)
first_coll, second_coll  = list(zip(*third_coll)) # (1, 2, 3, 4) (11, 12, 13, 14) пересборка исходных
# списков  NB!! исходники собираются в кортежи!!!
print(first_coll, second_coll)

