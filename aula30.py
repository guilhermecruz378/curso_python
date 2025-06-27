# CONSTANTE = são "variaveis usadas em letras maiusculas" que não vão mudar 
# Muitas condições no mesmo if é (Ruim) 
#   <- Contagem de complexidade (Ruim)

velocidade = 61  # velocidade atual do carro 
local_carro = 100 # local em que o carro está na estrada

RADAR_1 = 60  # velocidade maxima do radar 1 
LOCAL_1 = 100 # # local onde o radar 1 está 
RADAR_RANGE = 1 # A distância onde o radar pega

vel_carro_multado = velocidade > RADAR_1
local_do_range_1 = local_carro >= ( RADAR_RANGE - LOCAL_1) and \
      local_carro <= (RADAR_RANGE + LOCAL_1)
multado = vel_carro_multado and local_do_range_1

if multado:
    print(
        f'Seu veiculo foi multado no local {local_carro} \n' \
         f'onde era permitido a velocidade {RADAR_1}km/h você passou a {velocidade}km/h'
          )
else: 
    print('Dirija com cuidado!')