'''
Repetições
while (enquanto)
executa uma ação enquanto uma condição for verdadeira
loop infinito -> quando um código não tem fim
'''

condicao = True

while condicao:
    nome = input('Digite seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break

print('Acabou o código')
