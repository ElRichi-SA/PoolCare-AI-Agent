const contenido = document.getElementById("contenido");

export function vistaConsultaLibre() {
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

export function vistaGuiada() {
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
            
            <label>Aspecto del agua</label>
            <select id="aspecto">
                <option value="clara">Clara</option>
                <option value="nublada">Nublada</option>
                <option value="turbia">Turbia</option>
                <option value="verde">Verde</option>
            </select>
            <label>Temperatura del agua (°C)</label>
            <input id="temperatura" type="number" step="0.1">

            <button id="calcular">
                Obtener recomendación
            </button>

        </div>
    `;
}

export function renderDiagnosticos(lista) {
  if (!lista.length) return "";

  let html = `
        <div class="card">

            <h2>Diagnósticos</h2>
    `;

  lista.forEach((d) => {
    html += `

            <div class="diagnostico">

                <strong>${d.diagnostico}</strong>

                <br>

                Severidad:
                ${d.severidad}

            </div>

        `;
  });

  html += "</div>";

  return html;
}

export function renderTratamientos(lista) {
  if (!lista.length) return "";

  let html = `
        <div class="card">

            <h2>Tratamientos</h2>
    `;

  lista.forEach((t) => {
    html += `

            <div class="tratamiento">

                <strong>${t.producto}</strong>

                <br>

                Cantidad:

                ${t.cantidad}

                ${t.unidad}

                <br>

                ${t.procedimiento}

            </div>

        `;
  });

  html += "</div>";

  return html;
}

export function renderResultado(resultado) {
  return `

        ${renderDiagnosticos(resultado.diagnosticos)}

        ${renderTratamientos(resultado.tratamientos)}

        <div class="card">

            <h2>Respuesta de PoolCare AI</h2>

            <div style="white-space:pre-wrap">

                ${marked.parse(resultado.respuesta_llm)}

            </div>

        </div>

    `;
}

export function historial() {
  contenido.innerHTML = `
        <div class="card">
            <h2>Historial de Consultas</h2>
            <p>Aquí se mostrará el historial de consultas proximamente...</p>
        </div>
    `;
}

export function informacion() {
  contenido.innerHTML = `
        <div class="card">
            <h2>Información</h2>
            <p>PoolCare AI es una aplicación que ayuda a diagnosticar y recomendar tratamientos para piscinas.</p>
            <p>Aplicación desarrollada por Ricardo Salcedo como proyecto "Challenge" para Alura ONE.</p>
            <p>Repositorio: <a href="https://github.com/ElRichi-SA/PoolCare-AI-Agent" target="_blank">https://github.com/ElRichi-SA/PoolCare-AI-Agent</a></p>
        </div>
    `;
}
