"""script para validar  cpf"""


def tratar_cpf(cpf, config):
    new_cpf = list(cpf.replace(".", "").replace(" ", "").replace("-", ""))
    if config == 1:
        if len(new_cpf) == 11:
            return new_cpf
        else:
            return False

    else:
        if len(new_cpf) == 9:
            return new_cpf
        else:
            return False



def formato_cpf(cpf):
    cpf = ''.join(tratar_cpf(cpf, 1))
    formatado = f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"
    return formatado



def somar_valores(numeros):
    soma = 0

    for i, reverso in enumerate(range(len(numeros) + 1, 1, -1)):
        if not numeros[i].isnumeric():
            return False
        else:
            soma += (int(numeros[i]) * reverso)
    soma = 11 - (soma % 11)  # formula para gerar um cpf valido
    return soma


def verificar_validade(numeros):
    digitos = []
    if somar_valores(numeros):
        soma_primeiro_digito = somar_valores(numeros)

        if soma_primeiro_digito <= 9:
            numeros.append(str(soma_primeiro_digito))
            soma_segundo_digito = somar_valores(numeros)
            digitos.append(soma_primeiro_digito)

            if soma_segundo_digito <= 9:
                digitos.append(soma_segundo_digito)
                digitos.append(True)
                return digitos
            else:
                return False

        else:
            return False

    else:
        return False


# config: 1 = cpf completo, 2 = cpf sem dois últimos digitos
def validar_cpf(cpf, config):
    if config == 1:
        if type(tratar_cpf(cpf, config)) == list:
            numeros = tratar_cpf(cpf, config)[:9]

            if verificar_validade(numeros)[2]:
                return print(f"O CPF:{formato_cpf(cpf)} é valido!")
            else:
                return print(f"O CPF:{formato_cpf(cpf)} é invalido!")

    elif config == 2:
        if type(tratar_cpf(cpf, config)) == list:
            numeros = tratar_cpf(cpf, config)[:9]
            array = verificar_validade(numeros)
            return array



