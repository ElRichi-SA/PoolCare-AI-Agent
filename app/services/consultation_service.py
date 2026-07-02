class ConsultationService:

    @staticmethod
    def process(data):

        return {
            "estado": "ok",
            "datos_recibidos": {
                "volumen": data.volumen,
                "ph": data.ph,
                "cloro": data.cloro,
                "alcalinidad": data.alcalinidad,
                "aspecto": data.aspecto,
                "temperatura": data.temperatura
            },
            "diagnosticos": [],
            "tratamientos": [],
            "respuesta_llm": ""
        }