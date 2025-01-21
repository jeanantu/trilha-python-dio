numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}  ### ordena  vai removendo da pilha
print(numeros.pop())  # 0                         ### vai removendo da pilha
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

print()

numerosx = {4, 2, 3, 7, 8, 9, 5}
print(numerosx)  # {2, 3, 4, 5, 7, 8, 9}  ### ordena 
print(numerosx.pop())  # 2                ### vai removendo da pilha
print(numerosx.pop())  # 3
print(numerosx.pop())  # 4
print(numerosx)  # {5, 7, 8, 9}
