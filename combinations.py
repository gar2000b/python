# Combinations - e.g: how many different ways can you draw 3 pieces of fruit from 5 pieces.

from math import factorial as fac

n = 5
k = 3

result = fac(n) / (fac(k) * fac(n - k))
print("3 pieces of fruit from 5 total combi is: " + str(result))