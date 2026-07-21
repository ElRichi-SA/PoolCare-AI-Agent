# 🏊 PoolCare AI

**PoolCare AI** es un asistente inteligente para el análisis y mantenimiento de piscinas que combina reglas de negocio, recuperación de conocimiento (RAG) e Inteligencia Artificial Generativa para ofrecer diagnósticos, recomendaciones y tratamientos personalizados, basado en base de datos en archivos csv y pdf.

El sistema permite realizar consultas libres mediante lenguaje natural o utilizar un asistente guiado ingresando los parámetros químicos del agua(cloro, ph, alcalinidad, etc.).

---
## 🚀 Demo en línea

La aplicación está disponible en:

**https://poolcare-ai-agent-production.up.railway.app**

---
# Características

- 🤖 Consultas inteligentes mediante IA (Google Gemini).
- 📚 Sistema RAG (Retrieval-Augmented Generation) basado en documentación técnica.
- 🧪 Diagnóstico automático de parámetros del agua.
- 🧮 Cálculo automático de dosificación de productos químicos.
- 📄 Recomendaciones sustentadas en documentación técnica.
- 💻 Interfaz web moderna desarrollada con HTML, CSS y JavaScript.
- ⚡ API REST desarrollada con FastAPI.
- 📈 Arquitectura modular preparada para futuras ampliaciones.

---

# Arquitectura

```
Frontend
│
├── HTML
├── CSS
└── JavaScript
      │
      ▼
FastAPI
      │
      ▼
Servicios
│
├── ValidationService
├── DiagnosisService
├── TreatmentService
├── CalculationService
├── ConsultationService
└── HistoryService
      │
      ▼
RAG
│
├── Loader
├── Chunker
├── Embeddings
├── FAISS
└── Retriever
      │
      ▼
Google Gemini
```

---

# Tecnologías utilizadas

## Backend

- Python 3.13
- FastAPI
- Pydantic
- Pandas
- NumPy

## Inteligencia Artificial

- Google Gemini API
- LangChain
- HuggingFace Embeddings
- FAISS

## Frontend

- HTML5
- CSS3
- JavaScript (ES6)
- Bootstrap 5

## Base documental

- PDF
- CSV

---

# Estructura del proyecto

```
PoolCare-AI/

app/
│
├── api/
├── chat/
├── core/
├── llm/
├── models/
├── rag/
├── repositories/
├── services/
├── utils/
│
├── main.py
│
static/
│
├── css/
├── img/
└── js/
│
templates/
│
└── index.html
│
scripts/
│
tests/
│
docs/
```

---

# Flujo de funcionamiento

## Consulta libre

1. El usuario escribe una pregunta.
2. El sistema consulta la base documental mediante RAG.
3. Se recuperan los documentos más relevantes.
4. Se construye un prompt enriquecido.
5. Gemini genera una respuesta.
6. La respuesta se muestra en pantalla.

---

## Consulta guiada

1. El usuario captura los parámetros del agua.
2. Se validan los datos.
3. Se ejecuta el motor de reglas.
4. Se determinan los diagnósticos.
5. Se seleccionan los tratamientos.
6. Se calcula la dosificación.
7. Se consulta la documentación técnica.
8. Gemini genera una explicación detallada.
9. Se muestran diagnósticos, tratamientos y recomendaciones.

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/USUARIO/PoolCare-AI.git

cd PoolCare-AI
```

---

## Crear entorno virtual

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Variables de entorno

Crear un archivo `.env`

```env
GEMINI_API_KEY=TU_API_KEY
GEMINI_MODEL=gemini-2.5-flash
```

---

## Construir el índice vectorial

```bash
python -m scripts.build_index
```

---

## Ejecutar la aplicación

```bash
uvicorn app.main:app --reload
```

---

Abrir en el navegador

```
http://localhost:8000
```

---

# API

## Estado del servidor

```
GET /health
```

---

## Consulta libre

```
POST /consultar
```

Ejemplo

```json
{
  "consulta": "Mi piscina tiene agua verde."
}
```

---

## Consulta guiada

```
POST /analizar
```

Ejemplo

```json
{
  "volumen": 40,
  "ph": 6.8,
  "cloro": 0.2,
  "alcalinidad": 60,
  "aspecto": "verde",
  "temperatura": 28
}
```

---

# Estado del proyecto

Versión actual:

**v1.0.0**

Estado:

- ✅ MVP funcional
- ✅ Frontend integrado
- ✅ Backend operativo
- ✅ Motor de reglas
- ✅ Sistema RAG
- ✅ Integración con Google Gemini

---

# Próximas funcionalidades

- Historial persistente de consultas.
- Chat contextual con memoria.
- Gestión de clientes y piscinas.
- Reportes en PDF.
- Dashboard con métricas.
- Autenticación de usuarios.
- Despliegue en Oracle Cloud.

---

# Autor

**Ricardo Salcedo**

Proyecto desarrollado como una plataforma inteligente para el diagnóstico y mantenimiento de piscinas mediante Inteligencia Artificial Generativa, LLM y técnicas de Retrieval-Augmented Generation (RAG).
