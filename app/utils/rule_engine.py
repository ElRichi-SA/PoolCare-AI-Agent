import operator

OPERADORES = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne
}


def evaluar(valor_usuario, operador_txt, valor_regla):
    operador = OPERADORES[operador_txt]

    if isinstance(valor_usuario, str):
        return operador(
            valor_usuario.lower(),
            str(valor_regla).lower()
        )

    return operador(
        float(valor_usuario),
        float(valor_regla)
    )