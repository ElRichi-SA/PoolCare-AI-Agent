from app.repositories.diagnosis_repository import DiagnosisRepository
from app.utils.rule_engine import evaluate_rule


class DiagnosisService:

    def __init__(self):
        self.repository = DiagnosisRepository()

    def analyze(self, consultation):

        rules = self.repository.get_rules()

        diagnostics = []

        for _, rule in rules.iterrows():

            parameter = rule["parametro"]

            if parameter not in consultation:
                continue

            if evaluate_rule(
                consultation[parameter],
                rule["operador"],
                rule["valor"]
            ):

                diagnostics.append({
                    "diagnostico": rule["diagnostico"],
                    "severidad": rule["severidad"],
                    "codigo_tratamiento": rule["codigo_tratamiento"],
                    "mensaje": rule["mensaje"]
                })

        return diagnostics