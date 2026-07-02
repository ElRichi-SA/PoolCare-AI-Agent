from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

CSV_DIR = BASE_DIR / "data" / "csv"


class ValidationService:

    @staticmethod
    def validar_csv():

        archivos = [

            "productos.csv",

            "diagnosticos.csv",

            "dosificaciones.csv",

            "parametros_agua.csv",

            "procedimientos.csv",

            "compatibilidad_productos.csv"

        ]

        faltantes = []

        for archivo in archivos:

            if not (CSV_DIR / archivo).exists():

                faltantes.append(archivo)

        return faltantes