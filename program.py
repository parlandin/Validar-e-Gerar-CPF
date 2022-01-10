import verificar_cpf






print("Bem vindo ao validador de cpf")
while True:
    print("Opções: \n[1]Validar CPF \n[2]Gerar CPF\n[3]Sair")
    opcao = input("Sua escolha: ")
    if opcao == "1":
        user_cpf = input("Informe um cpf: ")
        print("------------------------------------- \n")
        verificar_cpf.validar_cpf(user_cpf)
        print("------------------------------------- \n")
    elif opcao == "2":
        exit()
        break
    else:
        print("Opção invalida! por favor, escolha uma opção valida.")











