import json
import pandas as pd

from app.database.connection import get_connection


class ConsultationRepository:

    def save(
        self,
        data,
        diagnosticos,
        tratamientos,
        respuesta
    ):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO consultas
            (
                fecha,
                ph,
                cloro,
                alcalinidad,
                temperatura,
                volumen,
                diagnosticos,
                tratamientos,
                respuesta
            )
            VALUES
            (
                CURRENT_TIMESTAMP,
                :1,
                :2,
                :3,
                :4,
                :5,
                :6,
                :7,
                :8
            )
        """, [

            data.ph,
            data.cloro,
            data.alcalinidad,
            data.temperatura,
            data.volumen,

            json.dumps(diagnosticos),

            json.dumps(
                tratamientos,
                ensure_ascii=False
            ),

            respuesta

        ])

        conn.commit()

        cursor.close()
        conn.close()