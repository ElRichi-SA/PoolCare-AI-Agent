import operator

OPERATORS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def evaluate_rule(value, operator_symbol, expected):

    if value is None:
        return False

    if operator_symbol not in OPERATORS:
        return False

    op = OPERATORS[operator_symbol]

    try:
        return op(float(value), float(expected))
    except ValueError:
        return op(str(value).lower(), str(expected).lower())