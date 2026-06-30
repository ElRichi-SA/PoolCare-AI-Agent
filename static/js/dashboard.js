import { consultarAPI } from "./api.js";
const contenido = document.getElementById("contenido");

function vistaConsultaLibre() {
  contenido.innerHTML = `
        <div class="card">
            <h3>Consulta Libre</h3>

            <textarea
                id="consulta"
                class="textarea"
                placeholder="Escribe aquí tu consulta..."
            ></textarea>

            <br><br>

            <button id="consultar">
                Consultar
            </button>
        </div>
    `;
}

function vistaGuiada() {
  contenido.innerHTML = `
        <div class="card">

            <h3>Asistente Guiado</h3>

            <label>Volumen de la piscina (m³)</label>
            <input id="volumen" type="number">

            <label>pH</label>
            <input id="ph" type="number" step="0.1">

            <label>Cloro libre (ppm)</label>
            <input id="cloro" type="number" step="0.1">

            <label>Alcalinidad</label>
            <input id="alcalinidad" type="number">

            <button id="calcular">
                Obtener recomendación
            </button>

        </div>
    `;
}

// Vista inicial
vistaConsultaLibre();

// Eventos de los botones superiores
document.getElementById("modoLibre").addEventListener("click", () => {
  vistaConsultaLibre();

  document.getElementById("modoLibre").classList.add("active");
  document.getElementById("modoGuiado").classList.remove("active");
});

document.getElementById("modoGuiado").addEventListener("click", () => {
  vistaGuiada();

  document.getElementById("modoGuiado").classList.add("active");
  document.getElementById("modoLibre").classList.remove("active");
});

document.addEventListener("click", async function (e) {
  if (e.target.id === "consultar") {
    const consulta = document.getElementById("consulta").value;

    const respuesta = document.getElementById("respuesta");

    respuesta.innerHTML = "Consultando...";

    try {
      const resultado = await consultarAPI({
        modo: "libre",

        consulta: consulta,
      });

      respuesta.innerHTML = `

        <div div class="spinner">
        
        ⏳ Consultando PoolCare AI...
        
        </div>
        
      `;
    } catch (error) {
      respuesta.innerHTML = `

            <div style="color:red">

            Error de comunicación con el servidor.

            </div>

            `;
    }
  }
});
