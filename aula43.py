# ---------- iniciando o laço for ----------

palavra = 'Python'

nova_string = ''
for letra in palavra:
    nova_string += f'*{letra}'
    print(letra)
print(nova_string + '*')