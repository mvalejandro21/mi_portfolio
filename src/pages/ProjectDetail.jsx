import React from 'react';
import { useParams } from 'react-router-dom';

export default function ProjectDetail() {
  const { id } = useParams();

  // Lógica real: fetch del contenido del proyecto
  return (
    <section className="py-20 px-6 container mx-auto max-w-3xl">
      <h3 className="text-3xl font-semibold mb-6">Detalles del proyecto: {id}</h3>

      <p className="mb-4">Este proyecto consiste en una limpieza y análisis exploratorio de datos, seguido por modelos predictivos.</p>

      <ul className="list-disc list-inside mb-6">
        <li><strong>Limpieza de datos:</strong> Eliminación de nulos, normalización de nombres, etc.</li>
        <li><strong>Análisis exploratorio:</strong> Visualización de tendencias y correlaciones</li>
        <li><strong>Modelos:</strong> Regresión, árboles de decisión, etc.</li>
      </ul>

      <p className="text-sm text-gray-500">Aquí puedes insertar enlaces a notebooks, Power BI, Colab o código en GitHub.</p>
    </section>
  );
}
