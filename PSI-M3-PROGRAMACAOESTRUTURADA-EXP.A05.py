def apresentar_questionario():
    print("Questionário de Satisfação")
    print("Por favor, responda às seguintes perguntas:")

    perguntas = [
        "1. Como avalia a infraestrutura da escola? (1-5)",
        "2. Como avalia a qualidade do atendimento? (1-5)",
        "3. Como avalia os equipamentos disponíveis? (1-5)",
        "4. Está satisfeito com a limpeza das instalações? (1-5)",
        "5. Recomenda esta escola a outras pessoas? (Sim/Não)",
        "6. Como avalia a qualidade do ensino? (1-5)",
    ]

    respostas = []
    for pergunta in perguntas:
        resposta = input(pergunta + " ")
        respostas.append(resposta)

    return respostas

def exportar_resultados(respostas):
    nome_ficheiro = input("Introduza o nome do ficheiro para guardar os resultados (ex: resultados.txt): ")
    try:
        with open(nome_ficheiro, "w") as ficheiro:
            ficheiro.write("Respostas ao Questionário de Satisfação\n")
            ficheiro.write("-" * 40 + "\n")
            perguntas = [
                "1. Avaliação da infraestrutura: ",
                "2. Avaliação do atendimento: ",
                "3. Avaliação dos equipamentos: ",
                "4. Satisfação com a limpeza: ",
                "5. Recomendação: "
            ]
            for pergunta, resposta in zip(perguntas, respostas):
                ficheiro.write(pergunta + resposta + "\n")
        print(f"Resultados guardados com sucesso no ficheiro '{nome_ficheiro}'.")
    except Exception as e:
        print(f"Erro ao guardar o ficheiro: {e}")

def main():
    while True:
        print("\nSistema de Questionário de Satisfação")
        print("1. Responder ao Questionário")
        print("2. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            respostas = apresentar_questionario()
            exportar_resultados(respostas)
        elif opcao == "2":
            print("Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
