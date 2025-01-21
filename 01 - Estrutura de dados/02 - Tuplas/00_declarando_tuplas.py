frutas = (
    "laranja",
    "pera",
    "uva",
)                ### diferença entre tupla e lista eh que tuplas nao podem ser modificadas. Esse eh objetivo tupla a garantia que nao sera modificada
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)   ### em tupla se coloca "," ao final para o interpretador ter a certeza que se trata de uma dupla
print(pais)
