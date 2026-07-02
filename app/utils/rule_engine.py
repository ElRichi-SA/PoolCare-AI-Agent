import operator

OPERATORS = {
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,
    "==": operator.eq,
    "!=": operator.ne,
}


def evaluate_rule(user_value, operator_symbol, rule_value):
    """
    Evalúa una regla de manera genérica.
    """

    op = OPERATORS[operator_symbol]

    if isinstance(user_value, str):
        return op(
            user_value.lower(),
            str(rule_value).lower()
        )

    return op(
        float(user_value),
        float(rule_value)
    )