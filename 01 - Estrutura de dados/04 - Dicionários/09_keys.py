contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])    retorna valor das chaves
print(resultado)


novo_contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},"a":{30},"nome":{"Jose"}}
print(novo_contatos.keys())