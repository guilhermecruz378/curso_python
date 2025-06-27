'''nome = 'Guilherme' 
novo_name = ''
cont = 0
while cont < len(nome):
    letra = nome[cont]
    #novo_name += f'*{letra}'
    novo_name = letra + '*'
    cont += 1
    print(novo_name, end='')'''

nome = 'Guilherme'
new_name = ''
num = 0
while num < len(nome):
    letra = nome[num]
    new_name += f'*{letra}'
    num += 1
print(new_name)

