'''
introdução ao try/except
try -> tentar executar o código
except -> ocorreu um erro ao tentar executar
'''

numero_str = input('Vou dobrar o número que você digitar: ')

try: 
    numero_float = float(numero_str)
    print('FLOAT', numero_float)
    print(f'O dobro do número {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um número')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')