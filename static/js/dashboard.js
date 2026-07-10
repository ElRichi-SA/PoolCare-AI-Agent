import { consultaLibre, consultaGuiada } from "./api.js";

import {
  vistaConsultaLibre,
  vistaGuiada,
  renderDiagnosticos,
  renderTratamientos,
  renderResultado,
} from "./views.js";

const contenido = document.getElementById("contenido");

// Vista inicial
vistaConsultaLibre();

// Botones de consulta
const modoLibreBtn = document.getElementById("modoLibre");
const modoGuiadoBtn = document.getElementById("modoGuiado");

// Eventos de los botones superiores
modoLibreBtn.addEventListener("click", () => {
  vistaConsultaLibre();

  modoLibreBtn.classList.add("active");
  modoGuiadoBtn.classList.remove("active");
});

modoGuiadoBtn.addEventListener("click", () => {
  vistaGuiada();

  modoGuiadoBtn.classList.add("active");
  modoLibreBtn.classList.remove("active");
});

// Eventos de consulta
document.addEventListener("click", async (e) => {
  if (e.target.id !== "consultar") return;

  const consulta = document.getElementById("consulta").value;
  const respuesta = document.getElementById("respuesta");

  respuesta.innerHTML = `
        <div class="spinner">
            ⏳ Analizando la información...
        </div>
    `;

  try {
    const resultado = await consultaLibre(consulta);

    respuesta.innerHTML = renderResultado(resultado);
  } catch (error) {
    respuesta.innerHTML = `
            <div class="card error">
                Error al conectar con el servidor.
            </div>
        `;

    console.error(error);
  }
});

document.addEventListener("click", async (e) => {
  if (e.target.id !== "calcular") return;

  const volumen = document.getElementById("volumen").value;
  const ph = document.getElementById("ph").value;
  const cloro = document.getElementById("cloro").value;
  const alcalinidad = document.getElementById("alcalinidad").value;
  const temperatura = document.getElementById("temperatura").value;
  const aspecto = document.getElementById("aspecto").value;
  const respuesta = document.getElementById("respuesta");

  respuesta.innerHTML = `
        <div class="spinner">
            ⏳ Analizando la información...
        </div>
    `;

  try {
    const resultado = await consultaGuiada({
      volumen: parseFloat(volumen),
      ph: parseFloat(ph),
      cloro: parseFloat(cloro),
      alcalinidad: parseFloat(alcalinidad),
      aspecto: aspecto,
      temperatura: parseFloat(temperatura),
    });

    respuesta.innerHTML = renderResultado(resultado);
  } catch (error) {
    respuesta.innerHTML = `
            <div class="card error">
                Error al conectar con el servidor.
            </div>
        `;

    console.error(error);
  }
});
// Botones laterales
const nuevaConsultaBtn = document.getElementById("nuevaConsulta");

// Eventos de los botones laterales
nuevaConsultaBtn.addEventListener("click", () => {
  if (modoLibreBtn.classList.contains("active")) {
    vistaConsultaLibre();
    modoLibreBtn.classList.add("active");
    modoGuiadoBtn.classList.remove("active");
  } else {
    vistaGuiada();
    modoGuiadoBtn.classList.add("active");
    modoLibreBtn.classList.remove("active");
  }
});
