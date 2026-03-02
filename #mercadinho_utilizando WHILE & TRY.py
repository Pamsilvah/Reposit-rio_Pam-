#mercadinho_utilizando WHILE & TRY
saldo = 0

while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver saldo")
    print("4 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            try:
                deposito = float(input("Valor para depositar: "))
                if deposito > 0:
                    saldo += deposito
                    print("Depósito realizado com sucesso!")
                else:
                    print("Digite um valor válido.")
            except:
                print("Digite apenas números.")

        elif opcao == 2:
            try:
                saque = float(input("Valor para sacar: "))
                if saque <= saldo and saque > 0:
                    saldo -= saque
                    print("Saque realizado com sucesso!")
                else:
                    print("Saldo insuficiente ou valor inválido.")
            except:
                print("Digite apenas números.")

        elif opcao == 3:
            print(f"Saldo atual: R$ {saldo:.2f}")

        elif opcao == 4:
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")

    except:
        print("Digite um número válido.")