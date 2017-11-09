#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique
import random


data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)

# Реализация задания 2
for i in data2:
    print(i, end=" ")

print()
unique = Unique(data1)

for u in unique:
    print(u, end= " ")
print()

str_list = ["Aa", "aa", "bb", "Bb"]
str_list2 = ["AA","aa","AA","aa"]
unique2 = Unique(str_list)

for u in unique2:
    print(u, end=" ")
print()


unique2 = Unique(str_list, ignore_case=True)
for u in unique2:
    print(u, end=" ")

