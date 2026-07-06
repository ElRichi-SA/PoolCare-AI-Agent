from app.repositories.diagnosis_repository import DiagnosisRepository
from app.utils.rule_engine import evaluate_rule


class DiagnosisService:

    def __init__(self):
        self.repository = DiagnosisRepository()

    def analyze(self, consultation):

        rules = self.repository.get_all_rules()

        diagnostics = []

        data = consultation.model_dump()

        for _, rule in rules.iterrows():

            parameter = rule["parametro"]

            if parameter not in data:
                continue

            value = data[parameter]

            if evaluate_rule(
                value,
                rule["operador"],
                rule["valor"]
            ):

                diagnostics.append({
                    "diagnostico": rule["diagnostico"],
                    "severidad": rule["severidad"],
                    "codigo_tratamiento": rule["codigo_tratamiento"]
                })

        return diagnostics