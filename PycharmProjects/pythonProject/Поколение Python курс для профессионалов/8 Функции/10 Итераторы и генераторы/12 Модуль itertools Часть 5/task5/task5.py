# Даны два множества A={1,2}, B={3,4}. Сопоставьте их декартовы произведения.
#
# Сопоставьте значения из двух списков
#
# A×B
# B×A
# A×A
# B×B

{(1,1),(1,2),(2,1),(2,2)}
{(3,3),(3,4),(4,3),(4,4)}
{(1,3),(1,4),(2,3),(2,4)}
{(3,1),(3,2),(4,1),(4,2)}

from  itertools import *

A={1,2}
B={3,4}

result = list(product(A, B))
print(result)
result = list(product(B, A))
print(result)
result = list(product(A, A))
print(result)
result = list(product(B, B))
print(result)