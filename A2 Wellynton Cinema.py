
while True:
    print("\n===== SISTEMA DE AVALIAÇÃO DO CINEMA =====")
    print("1. Cadastrar avaliação")
    print("2. Listar avaliações")
    print("3. Consultar estatísticas")
    print("4. Sair")

    opcao = input("Escolha uma opção:")

    if opcao == "1":
        idade = int(input("Digite a idade do cliente:"))

        print("1. Ótimo")
        print("2. Bom")
        print("3. Regular")
        print("4. Péssimo")

        avaliacao = input("Escolha a avaliação:")

        if avaliacao == "1":
            avaliacao = "Ótimo"
        elif avaliacao == "2":
            avaliacao = "Bom"
        elif avaliacao == "3":
            avaliacao = "Regular"
        elif avaliacao == "4":
            avaliacao = "Péssimo"
        else:
            print("Avaliação inválida!")
            avaliacao = ""

        if avaliacao != "":
            with open("avaliacoes.txt", "a", encoding="utf-8") as arquivo:
                arquivo.write(f"{idade};{avaliacao}\n")

            print("Avaliação cadastrada com sucesso!")

    elif opcao == "2":
        try:
            with open("avaliacoes.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Não existem avaliações cadastradas.")

            else:
                print("\n===== AVALIAÇÕES CADASTRADAS =====")

                for i in range(len(linhas)):
                    dados = linhas[i].strip().split(";")
                    idade = dados[0]
                    avaliacao = dados[1]

                    print(f"Cliente {i + 1} - Idade: {idade} - Avaliação: {avaliacao}")

        except FileNotFoundError:
            print("Não existem avaliações cadastradas.")

    elif opcao == "3":
        try:
            with open("avaliacoes.txt", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()

            if len(linhas) == 0:
                print("Não existem avaliações cadastradas.")

            else:
                otimo = 0
                bom = 0
                regular = 0
                pessimo = 0
                idades = []
                clientes = []

                for linha in linhas:
                    dados = linha.strip().split(";")
                    idade = int(dados[0])
                    avaliacao = dados[1]

                    idades.append(idade)
                    clientes.append([idade, avaliacao])

                    if avaliacao == "Ótimo":
                        otimo += 1
                    elif avaliacao == "Bom":
                        bom += 1
                    elif avaliacao == "Regular":
                        regular += 1
                    elif avaliacao == "Péssimo":
                        pessimo += 1

                maior = max(idades)
                menor = min(idades)

                print("\n===== ESTATÍSTICAS DAS AVALIAÇÕES =====")
                print(f"Total de respondentes: {len(linhas)}")
                print(f"Ótimo: {otimo}")
                print(f"Bom: {bom}")
                print(f"Regular: {regular}")
                print(f"Péssimo: {pessimo}")

                print("\nRespondente mais velho:")
                for cliente in clientes:
                    if cliente[0] == maior:
                        print(f"Idade: {cliente[0]} anos")
                        print(f"Avaliação: {cliente[1]}")
                        break

                print("\nRespondente mais novo:")
                for cliente in clientes:
                    if cliente[0] == menor:
                        print(f"Idade: {cliente[0]} anos")
                        print(f"Avaliação: {cliente[1]}")
                        break

        except FileNotFoundError:
            print("Não existem avaliações cadastradas.")

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
