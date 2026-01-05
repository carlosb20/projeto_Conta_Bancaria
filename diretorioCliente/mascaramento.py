def mascarar_email(email):
    try:
        nome, dominio = email.split("@")
    except ValueError:
        return "E-mail inválido"

    # Mantém somente os 3 primeiros caracteres do nome
    if len(nome) <= 3:
        nome_mascarado = nome[0] + "***"
    else:
        nome_mascarado = nome[:3] + "***"

    return f"{nome_mascarado}@{dominio}"

def mascarar_cpf(cpf):
    # Remove tudo que não seja número
    numeros = "".join(filter(str.isdigit, cpf))

    # Garante que tem 11 dígitos
    if len(numeros) != 11:
        return "CPF inválido"

    # Monta o CPF mascarado
    return f"***.***.{numeros[6:9]}-{numeros[9:]}"


def mascarar_telefone(telefone):
    # Remove tudo que não é número
    numeros = "".join(filter(str.isdigit, telefone))

    # Telefone precisa ter pelo menos 8 dígitos
    if len(numeros) < 8:
        return "Telefone inválido"

    # Mantém os dois primeiros e os dois últimos dígitos visíveis
    inicio = numeros[:2]
    fim = numeros[-2:]

    # Quantidade de dígitos que serão mascarados
    meio = "*" * (len(numeros) - 4)

    return f"{inicio}-{meio}{fim}"


def conta_bancaria_(numero):
    numero = str(numero)

    # últimos dígitos sempre será o DV
    corpo = numero[:-1]   # tudo menos o último
    dv = numero[-1]       # último dígito

    return f"{corpo}-{dv}"


# Exemplo de uso
