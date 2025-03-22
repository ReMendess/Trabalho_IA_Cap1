import time
import math
import os
import pandas as pd
import requests
import json

# culturas escolhidas , milho e soja
dados_culturas = []
# função para calcular insumos
def calcular_insumos(cultura, area_plantio):
    produto = str(input("Informe o nome do produto: "))
    dose_por_metro = float(input("Informe a dose por metro quadrado (mL/m²): "))
    total_insumos = dose_por_metro * area_plantio
    print(f"Para {area_plantio:.2f} m² de {cultura}, você precisará de {total_insumos:.2f} mL de {produto}.")
    return {"produto": produto, "dose_por_metro": dose_por_metro, "total": total_insumos}
# Menu Principal
def menu():
    while True:
        print("=== FarmTech Solutions ===")
        print("1. Adicionar cultura")
        print("2. Calcular manejo de insumos")
        print("3. Listar dados")
        print("4. Atualizar dados")
        print("5. Deletar dados")
        print("6. Sair")

        opcao = int(input("Escolha uma opcao: "))

        if opcao == 1:
            # cadastro de cultura e adicionando ela a lista inicial
            cultura = str(input("Informe a cultura (milho/soja): ")).lower().strip()
            dados_culturas.append({"cultura": cultura, "area": area_plantio, "insumos": []})
            print("Cultura {} cadastrada com sucesso!".format(cultura))

            # faz o calculo de insumos e coloca de acordo com o indice cadastrado anteriormente
        elif opcao == 2:
            print("\nCulturas cadastradas:")
            for i, cultura in enumerate(dados_culturas):
                print(f"{i} - {cultura['cultura']} (Área: {cultura['area']}m2)")
            index = int(input("Escolha a cultura pelo indice: "))
            insumos = calcular_insumos(dados_culturas[index]["cultura"], dados_culturas[index]["area"])
            dados_culturas[index]["insumos"].append(insumos)

            # apresenta os dados
        elif opcao == 3:
            if not dados_culturas:
                print("Nenhuma cultura cadastrada ainda.")
                time.sleep(2)
            else:
                for i, dado in enumerate(dados_culturas):
                    print(f"{i}: {dado['cultura']} - Área: {dado['area']:.2f} m²")
                    if dado["insumos"]:
                        print("Insumos: ")
                        for j, insumos in enumerate(dado["insumos"]):
                            print(f"      {j + 1}. {insumos['produto']} - {insumos['total']:.2f} mL")
                            time.sleep(3)
        elif opcao == 4:
            for i, dado in enumerate(dados_culturas):
                print(f"{i}: {dado['cultura']} - Área: {dado['area']:.2f} m²")

            index = int(input("Informe a posição do dado a ser atualizado: "))

            if 0 <= index < len(dados_culturas):
                nova_cultura = input("Informe a nova cultura (milho/soja): ").lower()
                nova_area = float(input("Informe a nova área em m²: "))

                dados_culturas[index]["cultura"] = nova_cultura
                dados_culturas[index]["area"] = nova_area
                dados_culturas[index]["insumos"] = None  # reseta os insumos

                print("Dados atualizados com sucesso!")
            else:
                print("Índice inválido. Tente novamente.")
        elif opcao == 5:
            for i, dado in enumerate(dados_culturas):
                print(f"{i}: {dado['cultura']} - Área: {dado['area']:.2f} m²")

            index = int(input("Informe a posição do dado a ser deletado: "))
            deletado = dados_culturas.pop(index)
            print(f"Dado '{deletado['cultura']}' removido.")
        elif opcao == 6:
            print(("encerrando programa..."))
            time.sleep(1)

            # Salvar os dados coletados em um arquivo CSV
            df = pd.DataFrame(dados_culturas)
            # Obter o diretório
            caminho_atual = os.path.dirname(os.path.abspath(__file__))
            caminho_arquivo = os.path.join(caminho_atual, "dados_agricultura.csv")

            # Salvar o arquivo
            df.to_csv(caminho_arquivo, index=False)
            print(f"Dados salvos em '{caminho_arquivo}'.")
            break

#funcao para obter cordenadas de uma cidade
def obter_coordenadas(cidade):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={cidade}&count=1&format=json"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if "results" in dados and len(dados["results"]) > 0:
            cidade_info = dados["results"][0]
            latitude = cidade_info["latitude"]
            longitude = cidade_info["longitude"]
            return latitude, longitude
    return None, None
# menu interativo principal
print("---------- Cadastro Inicial ----------")
nome = str(input("1 - Inserir nome: ")).strip()
sexo = str(input("2 - Masculino/Feminino [M/F]: ")).lower().strip()
idade = int(input("3 - Inserir Idade: "))
print("Fazendo cadastro...")
time.sleep(2)
if sexo == "f":
    print("Ola {}! Seja bem-vinda ao seu assistente de agricultura virtual! ".format(nome))
else:
    print("Ola {} ! Seja bem-vindo ao seu assistente de agricultura virtual ! ".format(nome))
time.sleep(1)

# definicao de formato de plantio
print("-" * 83)
formato_plantio = str(
    input("Digite Qual o formato do seu plantio: (Ex: Quadrado,Circular,Retangular,Triangulo): ")).lower()
while formato_plantio not in ["quadrado", "triangulo", "retangular", "circular"]:
    formato_plantio = str(
        input("Formato Invalido ! digite Qual o formato do seu plantio: (Ex: Quadrado,Circular,Retangular,Triangulo) "))
if formato_plantio == "quadrado":
    base = float(input("Digite qual a base do terreno: "))
    area_plantio = base ** 2
elif formato_plantio == "triangulo":
    base = float(input("Digite qual a base do terreno: "))
    altura = float(input("Digite qual altura do terreno: "))
    area_plantio = base * altura / 2
elif formato_plantio == "retangular":
    base = float(input("Digite qual a base do terreno: "))
    altura = float(input("Digite qual altura do terreno: "))
    area_plantio = base * altura
else:
    raio = float(input("Digite o raio do terreno: "))
    area_plantio = (raio ** 2) * 3.14
print("Calculando Area..")
time.sleep(1)

cidade = input("Informe o nome da cidade do terreno: ")
latitude, longitude = obter_coordenadas(cidade)
# Obter o diretório
caminho_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(caminho_atual, "coordenadas.csv")
# Abrir o arquivo e escrever os dados
with open(caminho_arquivo, "w") as f:
    f.write(f"{cidade},{latitude},{longitude}")

print(f"Dados salvos em '{caminho_arquivo}'.")


menu()
