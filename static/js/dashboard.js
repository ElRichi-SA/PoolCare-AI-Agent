import { consultaLibre, consultaGuiada } from "./api.js";

import {
  vistaConsultaLibre,
  vistaGuiada,
  renderDiagnosticos,
  renderTratamientos,
  renderResultado,
  historial,
  informacion,
} from "./views.js";

const contenido = document.getElementById("contenido");
const respuesta = document.getElementById("respuesta");
// Vista inicial
vistaConsultaLibre();

// Botones de consulta
const modoLibreBtn = document.getElementById("modoLibre");
const modoGuiadoBtn = document.getElementById("modoGuiado");

// Eventos de los botones superiores
modoLibreBtn.addEventListener("click", () => {
  vistaConsultaLibre();
  respuesta.hidden = false;

  modoLibreBtn.classList.add("active");
  modoGuiadoBtn.classList.remove("active");
});

modoGuiadoBtn.addEventListener("click", () => {
  vistaGuiada();
  respuesta.hidden = false;

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
  respuesta.hidden = false;

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
const historialBtn = document.getElementById("historial");
const informacionBtn = document.getElementById("informacion");

// Eventos de los botones laterales
nuevaConsultaBtn.addEventListener("click", () => {
  respuesta.hidden = false;
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

historialBtn.addEventListener("click", () => {
  historial();
  respuesta.hidden = true;
});
informacionBtn.addEventListener("click", () => {
  informacion();
  respuesta.hidden = true;
});
