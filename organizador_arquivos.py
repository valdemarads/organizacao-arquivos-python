import os
import shutil

def organizar_arquivos(caminho_pasta):
    if not os.path.isdir(caminho_pasta):
        print("Caminho inválido.")
        return

    for arquivo in os.listdir(caminho_pasta):
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)

        if os.path.isfile(caminho_arquivo):
            extensao = os.path.splitext(arquivo)[1].lower()

            if extensao == "":
                pasta_destino = os.path.join(caminho_pasta, "sem_extensao")
            else:
                pasta_destino = os.path.join(caminho_pasta, extensao.replace(".", ""))

            if not os.path.exists(pasta_destino):
                os.makedirs(pasta_destino)

            shutil.move(caminho_arquivo, os.path.join(pasta_destino, arquivo))

    print("Organização concluída com sucesso.")

if __name__ == "__main__":
    caminho = input("Digite o caminho da pasta que deseja organizar: ")
    organizar_arquivos(caminho)
