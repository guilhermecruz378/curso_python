import os
from time import sleep

lista = []
lista_vazia = []
lista_enumerada = enumerate(lista)

while True:
    print('Selecione uma opção')
    usuario = input('[i]nserir [a]pagar [l]istar:')

    if usuario == 'i':
        os.system('cls')
        valor_a_incluir = input('valor:')
        lista.append(valor_a_incluir)

    elif usuario == 'a':
        while True:
            try:
                indicie_a_apagar = input('qual indicie deseja apagar? ')
                indicie_int = int(indicie_a_apagar)
                lista.pop(indicie_int)
                break

            except ValueError:
                print('Não é possível apagar esse indicie: ')
                continue
            except IndexError:
                print('Selecione um num int.: ')
                continue
            except Exception:
                print('Erro desconhecido...')
                continue

    elif usuario == 'l':
        if lista == lista_vazia:
            print('não há oque exibir na lista')
            sleep(1)
        else:
            for indicie, itens in lista_enumerada:
                print(indicie, itens)
            sleep(1)

    
                
