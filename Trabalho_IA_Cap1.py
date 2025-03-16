import time
import math
import os

# culturas escolhidas , milho e soja

#menu interativo principal
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
#definicao de formato de plantio
print("-" * 83)
formato_plantio = str(input("Digite Qual o formato do seu plantio: (Ex: Quadrado,Circular,Retangular,Triangulo): ")).lower()
while formato_plantio not in ["quadrado", "triangulo", "retangular", "circular"]:
        formato_plantio = str(input("Formato Invalido ! digite Qual o formato do seu plantio: (Ex: Quadrado,Circular,Retangular,Triangulo) "))
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
print("A area do terreno corresponde a {:.2f} m2".format(area_plantio))
dados_culturas = []
def calcular_insumos(cultura, area_plantio):
    produto = input("Informe o nome do produto: ")
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
            #cadastro de cultura e adicionando ela a lista inicial
            cultura = str(input("Informe a cultura (milho/soja): ")).lower().strip()
            dados_culturas.append({"cultura": cultura, "area": area_plantio, "insumos": []})
            print("Cultura {} cadastrada com sucesso!".format(cultura))
            #faz o calculo de insumos e coloca de acordo com o indice cadastrado anteriormente
        elif opcao == 2:
            print("\nCulturas cadastradas:")
            for i, cultura in enumerate(dados_culturas):
                print(f"{i} - {cultura['cultura']} (Área: {cultura['area']}m2)")
            index = int(input("Escolha a cultura pelo indice: "))
            insumos = calcular_insumos(dados_culturas[index]["cultura"], dados_culturas[index]["area"])
            dados_culturas[index]["insumos"].append(insumos)
            #apresenta os dados
        elif opcao == 3:
            for i, dado in enumerate(dados_culturas):
                print(f"{i}: {dado['cultura']} - Área: {dado['area']:.2f} m²")
                if dado["insumos"]:
                    print("Insumos: ")
                    for j, insumos in enumerate (dado["insumos"]):
                        print(f"      {j + 1}. {insumos['produto']} - {insumos['total']:.2f} mL")
        elif opcao == 4:
            for i, dado in enumerate(dados_culturas):
                print(f"{i}: {dado['cultura']} - Área: {dado['area']:.2f} m²")

            index = int(input("Informe a posição do dado a ser atualizado: "))

            if 0 <= index < len(dados_culturas):
                nova_cultura = input("Informe a nova cultura (milho/soja): ").lower()
                nova_area = float(input("Informe a nova área em m²: "))

                dados_culturas[index]["cultura"] = nova_cultura
                dados_culturas[index]["area"] = nova_area
                dados_culturas[index]["insumos"] = None  #reseta os insumos

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
            break
menu()





