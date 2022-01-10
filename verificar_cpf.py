"""script para validar  cpf"""
"168.995.350-09"


def tratar_cpf(cpf):
    new_cpf = list(cpf.replace(".", "").replace(" ", "").replace("-", ""))
    if len(new_cpf) == 11:
        return new_cpf
    else:
        return print(f"O CPF:{cpf} é invalido!")

def formato_cpf(cpf):
    cpf = ''.join(cpf)
    formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
    return formatado



def somar_valores(numeros,cpf):
    soma = 0

    for i, reverso in enumerate(range(len(numeros) + 1, 1, -1)):
        if not numeros[i].isnumeric():
            return print(f"O CPF:{formato_cpf(tratar_cpf(cpf))} é invalido!")
        else:
            soma += (int(numeros[i]) * reverso)
    soma = 11 - (soma % 11)  # formula para gerar um cpf valido
    return soma


def verificar_validade(numeros, digitos, cpf):
    primeiro_digito = int(digitos[0])
    segundo_digito = int(digitos[1])
    soma_primeiro_digito = somar_valores(numeros, cpf)

    if soma_primeiro_digito <= 9 and soma_primeiro_digito == primeiro_digito:
        numeros.append(str(soma_primeiro_digito))
        soma_segundo_digito = somar_valores(numeros, cpf)

        if soma_segundo_digito <= 9 and soma_segundo_digito == segundo_digito:
            print(f"O CPF: '{formato_cpf(tratar_cpf(cpf))}' é valido!")

    else:
        return print(f"O CPF:{formato_cpf(tratar_cpf(cpf))} é invalido!")


def validar_cpf(cpf):
    if type(tratar_cpf(cpf)) == list:
        numeros = tratar_cpf(cpf)[:9]
        digitos = tratar_cpf(cpf)[9:12]
        verificar_validade(numeros, digitos, cpf)

