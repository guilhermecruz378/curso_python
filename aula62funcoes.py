"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""


# def soma(x, y, z):
#     # Definição
#     print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


# soma(1, 2, 3)
# soma(1, y=2, z=5)

# print(1, 2, 3, sep='-')

def soma(x=0 , y=0, z=0):
    somando = x + y + z
    print(somando)
soma(1,z=2, y=8)