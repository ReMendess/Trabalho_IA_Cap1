import math

dados_culturas = []


def calcular_area(cultura):
    if cultura == "milho":
        base = float(input("Informe a base do retângulo (m): "))
        altura = float(input("Informe a altura do retângulo (m): "))
        return base * altura
    elif cultura == "soja":
        raio = float(input("Informe o raio da área circular (m): "))
        return math.pi * (raio ** 2)
    else:
        print("Cultura não cadastrada.")
        return 0


def calcular_insumos(cultura):
    produto = input("Informe o nome do produto: ")
    dose_por_metro = float(input("Informe a dose por metro quadrado (mL/m²): "))
    area = calcular_area(cultura)
    total_insumos = dose_por_metro * area
    print(f"Para {area:.2f} m², você precisará de {total_insumos:.2f} mL de {produto}.")
    return total_insumos


def menu():
    while True:
        print("\n=== FarmTech Solutions ===")
        print("1. Adicionar cultura")
        print("2. Calcular área de plantio")
        print("3. Calcular manejo de insumos")
        print("4. Listar dados")
        print("5. Atualizar dados")
        print("6. Deletar dados")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cultura = input("Informe a cultura (milho/soja): ").lower()
            dados_culturas.append(cultura)
        
        elif opcao == "2":
            cultura = input("Informe a cultura para calcular a área: ").lower()
            area = calcular_area(cultura)
            print(f"Área calculada: {area:.2f} m²")
        
        elif opcao == "3":
            cultura = input("Informe a cultura para calcular insumos: ").lower()
            calcular_insumos(cultura)
        
        elif opcao == "4":
            print("Dados cadastrados:", dados_culturas)
        
        elif opcao == "5":
            index = int(input("Informe a posição do dado a ser atualizado: "))
            nova_cultura = input("Informe a nova cultura: ").lower()
            if 0 <= index < len(dados_culturas):
                dados_culturas[index] = nova_cultura
            else:
                print("Posição inválida.")
        
        elif opcao == "6":
            index = int(input("Informe a posição do dado a ser deletado: "))
            if 0 <= index < len(dados_culturas):
                deletado = dados_culturas.pop(index)
                print(f"Dado '{deletado}' removido.")
            else:
                print("Posição inválida.")
        
        elif opcao == "7":
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()


