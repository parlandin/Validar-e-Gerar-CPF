"""script para validar ou gerar um cpf"""
"168.995.350-09"



def tratar_cpf(cpf):
    new_cpf = list(cpf.replace(".", "").replace(" ", ""))
    if len(new_cpf) == 12:
        return new_cpf
    else:
        return print(f"O CPF:{cpf} é invalido!")


def somar_valores(numeros):
    soma = 0

    for i, reverso in enumerate(range(len(numeros) + 1, 1, -1)):
        if not numeros[i].isnumeric():
            return print(f"O CPF:{''.join(tratar_cpf(user_cpf))} é invalido!")
        else:
            soma += (int(numeros[i]) * reverso)
    soma = 11 - (soma % 11)  # formula para gerar um cpf valido
    return soma

def verificar_validade(numeros, digitos):
    primeiro_digito = int(digitos[0])
    segundo_digito = int(digitos[1])
    soma_primeiro_digito = somar_valores(numeros)

    if soma_primeiro_digito <= 9 and soma_primeiro_digito == primeiro_digito:
        numeros.append(str(soma_primeiro_digito))
        soma_segundo_digito = somar_valores(numeros)

        if soma_segundo_digito <= 9 and soma_segundo_digito == segundo_digito:
            print(f"O CPF: '{''.join(tratar_cpf(user_cpf))}' é valido!")

    else:
        return print(f"O CPF:{''.join(tratar_cpf(user_cpf))} é invalido!")


def validar_cpf(cpf):
    if type(tratar_cpf(cpf)) == list:
        numeros = tratar_cpf(cpf)[:9]
        digitos = tratar_cpf(cpf)[10:12]
        verificar_validade(numeros, digitos)

print("Bem vindo ao validador de cpf")
while True:
    print("Opções: \n[1]Validar CPF \n[2]Sair")
    opcao =input("Sua escolha: ")
    if opcao == "1":
        user_cpf = input("Informe um cpf: ")
        print("------------------------------------- \n")
        validar_cpf(user_cpf)
        print("------------------------------------- \n")
    elif opcao == "2":
        exit()
        break
    else:
        print("Opção invalida! por favor, escolha uma opção valida.")

