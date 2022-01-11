import random
import verificar_cpf

"""script para gerar CPF"""

def gerar_num_aleatorio():
    num_aleat = ''
    for i in range(3):
        num_aleat += str(random.randrange(0, 9))
    return num_aleat

def gerar_cpf():
    cpf = f"{gerar_num_aleatorio()}.{gerar_num_aleatorio()}.{gerar_num_aleatorio()}"
    return cpf

def validar_e_retorna():
    while True:
        cpf = gerar_cpf()
        novo_cpf = verificar_cpf.validar_cpf(cpf, 2)

        if novo_cpf:
            cpf_valido = f"{cpf}-{novo_cpf[0]}{novo_cpf[1]}"
            break
        else:
            continue
    return cpf_valido



