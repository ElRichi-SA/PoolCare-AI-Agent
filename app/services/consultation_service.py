class ConsultationService:

    @staticmethod
    def process(data):

        if data.modo == "libre":

            return {
                "estado": "ok",
                "respuesta": f"Consulta recibida: {data.consulta}"
            }

        return {
            "estado": "ok",
            "respuesta": (
                f"Volumen: {data.volumen} m³ | "
                f"pH: {data.ph} | "
                f"Cloro: {data.cloro}"
            )
        }