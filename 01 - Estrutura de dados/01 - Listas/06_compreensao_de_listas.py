# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]  ###### ==>>> compreensao o 1 "numero" corresponde ao retorno da iteracao
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]               ###### ==>>> compreensao o 1 "numero" corresponde ao retorno da iteracao, ex. for numero in numeros o retorno joga em numero
print(quadrado)                                            ###### ==>>> obs. o retorno precisa ter o mesmo nome do iterador


numerosx = [1, 30, 21, 2, 9, 65, 34,190,1030,4040,12,56,789,34,56,78]
numerosx = list(set(numerosx))  ### removendo duplicidades
numerosx.sort()                 ### ordenando a lista
nova_lista = []
for numero in numerosx:                                    ###### ==>>> sem compreensao
    if numero % 2 == 0:
        nova_lista.append(numero) ### preenchendo a nova lista com numeros pares
print(nova_lista)        
        



