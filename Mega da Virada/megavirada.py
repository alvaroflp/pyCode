import random
import megaresultados

def mega_virada(jogos_anteriores, num_combinacoes, num_numeros_por_combinacao):
    contagem_numeros = {}
    total_numeros = 0

    for jogo in jogos_anteriores:
        for numero in jogo:
            if numero in contagem_numeros:
                contagem_numeros[numero] += 1
            else:
                contagem_numeros[numero] = 1
            total_numeros += 1

    probabilidade_numeros = {numero: contagem / total_numeros for numero, contagem in contagem_numeros.items()}

    # Gera combinações com base na probabilidade
    combinacoes_geradas = []

    for _ in range(num_combinacoes):
        combinacao = random.choices(list(probabilidade_numeros.keys()), weights=list(probabilidade_numeros.values()), k=num_numeros_por_combinacao)
        combinacoes_geradas.append(combinacao)

    return combinacoes_geradas

def main():
    jogos_anteriores = megaresultados.resultados

    num_combinacoes = int(input("Digite o número de combinações a serem geradas: "))
    num_numeros_por_combinacao = 6  

    combinacoes = mega_virada(jogos_anteriores, num_combinacoes, num_numeros_por_combinacao)

    for i, combinacao in enumerate(combinacoes, 1):
        combinacao_formatada = "-".join(map(str, combinacao))
        print(f"Combinação {i}: {combinacao_formatada}")

if __name__ == "__main__":
    main()
