const boton = document.getElementById("btnConsultar");

boton.addEventListener("click", () => {
  const consulta = document.getElementById("consulta").value;

  const respuesta = document.getElementById("respuesta");

  respuesta.innerHTML = "<b>Consulta enviada:</b><br><br>" + consulta;
});

document.addEventListener("click", function (e) {
  if (e.target.id === "consultar") {
    const texto = document.getElementById("consulta").value;

    document.getElementById("respuesta").innerHTML =
      "<h3>Consulta enviada</h3><br>" + texto;
  }
});
