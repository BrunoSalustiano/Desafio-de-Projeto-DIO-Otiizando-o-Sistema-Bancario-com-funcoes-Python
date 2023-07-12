import textwrap

def menu():
    menu = """
    =============== MENU ===============
    [D]\t Depositar
    [S]\t Sacar
    [E]\t Extrato
    [C]\t Abrir Conta
    [L]\t Listar Contas
    [N]\t Novo Cliente
    [Q]\t Sair
    """
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0 :
        saldo += valor
        extrato += f"Depósito: \tR$ {valor:.2f}\n"
        print("=== Depósito realizado com sucesso! ===")

    else:
        print("### Operacao Falhou! O valor informado e invalido ###")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, n_saques, lim_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = n_saques > lim_saques

    if excedeu_saldo:
        print("### Saldo insuficiente para realizar a operacao! ###")

    elif excedeu_limite:
        print("### Valor informado maior que limite maximo para operacao! ###")

    elif excedeu_saques:
        print("### Numero limite de saques ja realizado! ###")

    elif valor > 0:
        saldo -= valor
        n_saques += 1
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        print("=== Saque realizado com sucesso! ===")

    else:
        print("### Valor informado invalido. Operacao nao realizada! ###")

    return saldo, extrato

def mostra_extrato(saldo,/,*, extrato):
    print("\n=============== EXTRATO===============\n")
    print("Não foram realizadas movimentações na conta.\n" if not extrato else extrato)
    print("=============================================\n")
    print(f"Saldo da conta: R$ {saldo:.2f}\n ")
    print("=============================================\n")


def cria_cliente(clientes):
    cpf = input("Iforme o CPF (Somente Numeros): ")
    cliente = filtra_clientes(cpf, clientes)

    if cliente:
        print("### Ja existe cliente para o CPF informado ###")
        return
    
    nome = input("Nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente (dd-mm-aaaa): ")
    endereco = input("Informe o endereco (lagradouro, numero - bairro - cidade/estado): ")

    clientes.append({"nome": nome, "data_nascimento":data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Cliente cadastrado com sucesso! ===")

def filtra_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente["cpf"] == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def cria_conta(agencia, numero_conta, clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtra_clientes(cpf, clientes)

    if cliente:
        print("\n===  Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente}
    
    print("### Usuario nao encontrado. Impossivel abrir conta! ###")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            Conta:\t{conta['numero_conta']}
            Cliente:\t{conta['cliente']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    n_saques = 0
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                n_saques=n_saques,
                lim_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            mostra_extrato(saldo, extrato = extrato)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = cria_conta(AGENCIA, numero_conta, clientes)

            if conta:
                contas.append(conta)
        
        elif opcao == "l":
            lista_contas(contas)

        elif opcao == "n":
            cria_cliente(clientes)

        elif opcao == "q":
            break

        else:
            print("Opcao invalida. Por gentileza selecione uma opcao valida.")


main()

