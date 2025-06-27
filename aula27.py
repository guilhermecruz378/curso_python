'''Fatiamento de strings

indicie a contar do número 0(zero)
contagem de caracter a contar do número 1(um)

 012345678
 olá mundo
-987654321
Fatiamento [i:f:p]==[inicio, final, passo] [::]
obs.: a função len retorna a qtd 
de caracter da str / checar a qtd da string

'''
variavel = 'olá mundo'
print(variavel)
print(len(variavel[0:9:1]))
print(len(variavel[::1]))
print('-='*10)
print(variavel[::-1])
print(len(variavel[::-1]))
print(len(variavel[-10:-1:1]))