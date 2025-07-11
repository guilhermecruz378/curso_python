""" imprecisão no float => é corrgido com uma função no python 
chamada (round) => ela arredonda um número

Ou pode ser corrigido usando modulos importados do proprio python
geralmente esse modulo é usado quando é preciso calcular um número
muito preciso no programa.
"""
import decimal


# numero1 = decimal.Decimal(0.1)
# numero2 = decimal.Decimal(0.7)
numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.7')
numero3 = numero1 + numero2

print(numero3)
print(f'{numero3:.2f}')
print(round(numero3, 10))
#        passa o num, qtd de casas