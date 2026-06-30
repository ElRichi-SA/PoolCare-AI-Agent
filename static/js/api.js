export async function consultarAPI(datos) {
  const respuesta = await fetch("/consultar", {
    method: "POST",

    headers: {
      "Content-Type": "application/json",
    },

    body: JSON.stringify(datos),
  });

  if (!respuesta.ok) {
    throw new Error("Error al consultar el servidor.");
  }

  return await respuesta.json();
}
