import "./dashboard.js";

document.addEventListener("click", function (e) {
  if (e.target.id === "consultar") {
    const consulta = document.getElementById("consulta").value;

    document.getElementById("respuesta").innerHTML = `
            <h3>Consulta enviada</h3>
            <p>${consulta}</p>
        `;
  }

  if (e.target.id === "calcular") {
    document.getElementById("respuesta").innerHTML = `
            <h3>Resultado</h3>

            <p>En la siguiente fase aquí aparecerá el cálculo de dosificación.</p>
        `;
  }
});
