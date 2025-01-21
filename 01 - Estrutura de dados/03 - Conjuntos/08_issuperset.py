conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False contrario do issubset... todos os elementos de a estao em b ?
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)
