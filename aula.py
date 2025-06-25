velocidade = 61
local_carro = 98

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

carro_passou_no_radar = velocidade > RADAR_1
carr_passou_no_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) 
carro_multado = carr_passou_no_radar1 and carro_passou_no_radar


if carro_passou_no_radar:
    print('velocidade do carro maior que o radar')

#if carro_passou:
#    print('carro passou radar 1')

if carro_multado:
    print('multado, em radar 1')
