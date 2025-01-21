linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

linguagens = ["python", "java", "c", "java", "csharp"]
print(linguagens.index("java"))  # 1    o index se limita a trazer apenas a 1 ocorrencia, havendo duplicidade pega a primeira