export function vistaConsultaLibre() {
  return `

<textarea
id="consulta"
placeholder="Escribe aquí tu consulta..."
class="textarea">
</textarea>

<button id="consultar">

Consultar

</button>

`;
}

export function vistaGuiada() {
  return `

<div class="card">

<label>

Volumen de la piscina (m³)

</label>

<input id="volumen" type="number">

<label>

pH

</label>

<input id="ph" type="number" step="0.1">

<label>

Cloro Libre (ppm)

</label>

<input id="cloro" type="number" step="0.1">

<label>

Alcalinidad

</label>

<input id="alcalinidad" type="number">

<button id="calcular">

Obtener recomendación

</button>

</div>

`;
}
