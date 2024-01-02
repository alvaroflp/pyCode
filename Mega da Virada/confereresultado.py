# Definindo os números ganhadores
numeros_ganhadores = [24, 56, 33, 48, 21, 41]

# Definindo as apostas
apostas = {
    132577007: [[8,27,39,46,54,56],[14,16,31,48,51,59],[2,16,20,48,57,58],[7,14,21,22,25,46],[5,26,30,47,48,50],[3,16,17,22,23,31],[1,18,35,42,46,50],[4,19,25,44,50,59],[8,12,23,38,40,43],[4,18,25,34,47,56],[5,6,10,14,19,55],[1,11,13,28,36,54],[18,37,38,40,55,60],[6,12,24,30,32,44],[9,15,37,38,58,59],[9,44,46,51,54,55],[5,17,27,38,48,50],[3,19,26,32,36,49]],
    179887622: [[2,11,24,33,36,52],[12,14,33,34,48,55],[3,5,7,47,50,54],[1,2,4,6,26,48],[9,19,20,25,32,33],[7,10,17,20,31,56]],
    180598335: [[2,8,16,23,37,50],[5,11,22,24,51,53],[9,15,37,38,39,59],[5,14,15,35,41,60],[9,25,32,38,48,60],[2,3,4,25,40,56]],
    183951882: [[12,18,29,32,38,44],[13,28,39,41,44,50],[7,11,38,40,45,46],[12,16,18,23,38,44],[3,14,16,50,54,57],[9,10,11,25,50,60]]
}

# Função para contar os pontos de um jogo específico
def contar_pontos(aposta):
    pontos = 0
    for numero in aposta:
        if numero in numeros_ganhadores:
            pontos += 1
    return pontos * 10  # Cada número acertado vale 10 pontos

# Verificando os pontos para cada aposta
for chave, lista_aposta in apostas.items():
    print(f"Aposta {chave}:")
    pontuacao_por_jogo = {}  # Dicionário para armazenar a pontuação por jogo
    for idx, aposta in enumerate(lista_aposta, start=1):
        pontos = contar_pontos(aposta)
        pontuacao_por_jogo[f"Jogo {idx}"] = pontos
        print(f"   Jogo {idx}: {pontos} pontos - Números: {aposta}")
    
    # Determinando o jogo com maior pontuação
    jogo_max_pontos = max(pontuacao_por_jogo, key=pontuacao_por_jogo.get)
    print(f"Jogo com maior pontuação: {jogo_max_pontos} com {pontuacao_por_jogo[jogo_max_pontos]} pontos\n")

