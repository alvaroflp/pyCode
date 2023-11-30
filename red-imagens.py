'''
necessário: pip install pillow
'''

import os
from PIL import Image

def redimensionar_imagens(diretorio_entrada, diretorio_saida, largura, altura):

    if not os.path.exists(diretorio_saida):
        os.makedirs(diretorio_saida)

    lista_arquivos = os.listdir(diretorio_entrada)

    for arquivo in lista_arquivos:
        if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
  
            caminho_entrada = os.path.join(diretorio_entrada, arquivo)
            caminho_saida = os.path.join(diretorio_saida, f"{os.path.splitext(arquivo)[0]}_red{os.path.splitext(arquivo)[1]}")

            imagem = Image.open(caminho_entrada)
            nova_imagem = imagem.resize((largura, altura))
            nova_imagem.save(caminho_saida)

            print(f"{arquivo} redimensionado e salvo como {os.path.basename(caminho_saida)}")

# Exemplo de uso
diretorio_entrada = r'C:\img\orig'
diretorio_saida = r'C:\img\red'
largura_desejada = 800
altura_desejada = 600

redimensionar_imagens(diretorio_entrada, diretorio_saida, largura_desejada, altura_desejada)
