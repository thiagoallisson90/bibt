import math

# Função para calcular a probabilidade de colisão com Poisson
def calc_prob_colisao(n, lambda_n, toa):
    # Taxa total de transmissão (lambda total)
    lambda_total = n * lambda_n
    
    # Cálculo da probabilidade de colisão
    prob_colisao = 1 - math.exp(-lambda_total * toa)
    return prob_colisao

# Função para calcular a quantidade máxima de EDs para um SF específico
def calc_max_eds_per_sf(toa, lambda_n, threshold=0.01):
    n = 1  # Começa com 1 dispositivo
    while True:
        # Calcular a probabilidade de colisão
        prob_colisao = calc_prob_colisao(n, lambda_n, toa)
        
        # Calcular a probabilidade de sucesso
        prob_sucesso = 1 - prob_colisao
        
        # Se a probabilidade de sucesso for menor que o threshold, parar
        if prob_sucesso < (1 - threshold):  # Threshold de 99% de sucesso
            return n - 1  # Retorna o valor de n anterior
        n += 1

# ToAs fornecidos para cada SF em segundos
toa_values = {7: 0.112896, 8: 0.205312, 9: 0.369664, 10: 0.657408, 11: 1.2329, 12: 2.30195}

# Parâmetros
lambda_n = 0.1  # Taxa de chegada de pacotes por dispositivo (pacotes por segundo)
threshold = 0.01  # Taxa de falha máxima permitida (1% de falha, ou 99% de sucesso)

# Função principal para calcular o número máximo de EDs para cada SF
def calc_max_eds_all_sf(lambda_n, toa_values, threshold=0.01):
    max_eds_per_sf = {}
    
    # Iterar sobre os SFs e calcular o número máximo de EDs para cada um
    for sf, toa in toa_values.items():
        max_eds = calc_max_eds_per_sf(toa, lambda_n, threshold)
        max_eds_per_sf[sf] = max_eds
    
    return max_eds_per_sf

# Cálculo da quantidade máxima de EDs por SF
max_eds_by_sf = calc_max_eds_all_sf(lambda_n, toa_values, threshold)
print("Quantidade máxima de EDs por SF para 99% de taxa de sucesso:", max_eds_by_sf)
