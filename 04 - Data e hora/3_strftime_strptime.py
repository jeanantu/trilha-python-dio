from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2023-10-20 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_ptbr1 = "%d/%m/%Y %H:%M:%S"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))
print(data_hora_atual.strftime(mascara_ptbr1))

data_convertida = datetime.strptime(data_hora_str, mascara_en) ### fazendo parser (conversao)
print(data_convertida)
print(type(data_convertida))
print(type(data_hora_str))

print(data_convertida.strftime("%Y"))
print(data_hora_atual.strftime("%Y"))