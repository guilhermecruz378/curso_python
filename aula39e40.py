#calculadora usando while
from time import sleep
while True:
    numero1 = input('Digite um número: ')
    numero2 = input('Digite outro número: ')
    operador = input('Digite um operador (+-/*)')
    numeros_validos = None

    numero1_float = 0
    numero2_float = 0

    try:
        numero1_float = float(numero1)
        numero2_float = float(numero2)
        numeros_validos = True

    except:
        numeros_validos = None
    
    if numeros_validos is None:
        print('Um ou Ambos os números está inválidos.')
        continue

    operadores_validos = '+-/*'
    if operador not in operadores_validos:
        print('Operador inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Calculando o resultado. Confira a baixo... ')
    sleep(1)

    if operador == '+':
        print(f'{numero1_float} + {numero2_float} = ',numero1_float + numero2_float)
    elif operador == '-':
        print(f'{numero1_float} - {numero2_float} = ',numero1_float - numero2_float)
    elif operador == '/':
        print(f'{numero1_float} / {numero2_float} = ',numero1_float / numero2_float)
    elif operador == '*':
        print(f'{numero1_float} * {numero2_float} = ',numero1_float * numero2_float)
    else:
        print('Nunca deveria chegar aqui. ')

    sair = input('Deseja Sair: [s/n] ').lower().startswith('s')

    if sair is True:
        break

print('Saindo do programa...')
for c in range(0, 4):
    print(f'{c}...',end=' ')
    sleep(1)
print('\nPrograma finalizado.')