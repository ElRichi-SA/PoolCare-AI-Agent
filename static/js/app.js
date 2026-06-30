const boton = document.getElementById("btnConsultar");

boton.addEventListener("click", () => {
  const consulta = document.getElementById("consulta").value;

  const respuesta = document.getElementById("respuesta");

  respuesta.innerHTML = "<b>Consulta enviada:</b><br><br>" + consulta;
});
