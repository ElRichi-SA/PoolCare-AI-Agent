from app.repositories.calculation_repository import CalculationRepository


class CalculationService:

    def __init__(self):
        self.repository = CalculationRepository()

    def calculate(self, volumen, tratamientos):

        dosages = self.repository.get_dosages()

        result = []

        for tratamiento in tratamientos:

            id_producto = tratamiento["id_producto"]

            row = dosages[
                dosages["id_producto"] == id_producto
            ]

            if row.empty:
                tratamiento["cantidad"] = None
                tratamiento["unidad"] = ""
                result.append(tratamiento)
                continue

            row = row.iloc[0]

            cantidad = (
                volumen /
                float(row["volumen_base"])
            ) * float(row["dosis_base"])

            tratamiento["cantidad"] = round(cantidad, 2)
            tratamiento["unidad"] = str(row["unidad"])

            result.append(tratamiento)

        return result