"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

#print(sum(numeros))
# print(*numeros)


# def soma(*args):
    
#     acumulador = 0 
#     for numeros in args:
#         acumulador += numeros
#     return acumulador

# numeros_tupla = 1,2,3,4,5,6,7,8,9

# soma1 = soma(4, 6, 7, 8, 9, 0, 10)
# soma2 = soma(*numeros_tupla)
# print(soma1)
# print(soma2)

