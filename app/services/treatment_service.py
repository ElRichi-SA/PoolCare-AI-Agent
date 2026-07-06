from app.repositories.treatment_repository import TreatmentRepository

class TreatmentService:

    def __init__(self):
        self.repository = TreatmentRepository()

    def build(self, diagnostics):

        treatments = self.repository.get_all()
        products = self.repository.get_products()
        procedures = self.repository.get_procedures()

        result = []

        for diagnosis in diagnostics:

            code = diagnosis["codigo_tratamiento"]

            matches = treatments[
                treatments["codigo_tratamiento"] == code
            ]

            for _, row in matches.iterrows():

                product = products[
                    products["id_producto"] == row["id_producto"]
                ].iloc[0]

                procedure = procedures[
                    procedures["id_procedimiento"] == row["id_procedimiento"]
                ].iloc[0]

                result.append({
                    "codigo": str(code),
                    "id_producto": int(product["id_producto"]),
                    "producto": str(product["nombre"]),
                    "procedimiento": str(procedure["titulo"])
                })

        return result