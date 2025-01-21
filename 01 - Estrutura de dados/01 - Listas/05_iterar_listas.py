carros = ["gol", "celta", "palio"]
nomes = ["joao","joaquim","pedro","judas","tiago","simao","tadeu","lucas","mateus","marcos"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

print()

nomes.sort()     ## aplicando ordenacao 
for index, nome in enumerate(nomes):
    print(f"{index}: - {nome}")