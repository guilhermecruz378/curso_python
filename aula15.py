# a função input é usada para coletar dados do usuario
# quando o usuario digitar na function input o valor é armazenado como str

numero1 = input('Digite um número: ') 
numero2 = input('Digite outro número: ')

int_numero_1 = int(numero1)
int_numero_2 = int(numero2)

print(f'A soma dos números são {int_numero_1 + int_numero_2}')
