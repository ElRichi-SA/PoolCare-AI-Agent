const API = "";

export async function consultaLibre(texto) {
  const response = await fetch(`${API}/consultar`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      consulta: texto,
    }),
  });

  if (!response.ok) {
    throw new Error("Error al consultar el servidor");
  }

  return await response.json();
}

export async function consultaGuiada(datos) {
  const response = await fetch(`${API}/analizar`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(datos),
  });

  if (!response.ok) {
    throw new Error("Error al analizar");
  }

  return await response.json();
}

export async function health() {
  const response = await fetch(`${API}/health`);

  return await response.json();
}
