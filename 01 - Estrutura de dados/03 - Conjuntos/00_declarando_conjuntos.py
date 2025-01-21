numeros = set([1, 2, 3, 1, 3, 4]) #### usando lista internamente
print(numeros)  # {1, 2, 3, 4}   ### set nao aceita duplicidade mas não garante a ordem

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio")) ### usando tupla internamente
print(carros)  # {"gol", "celta", "palio"}

conjunto = {"python","java","c","python"}  ### outra forma criar conjunto, veja que a ordem foi alterada na saida
print(conjunto) # {'c', 'python', 'java'}
