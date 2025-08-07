import React from 'react';

export default function CV() {
  return (
    <section className="py-20 px-6 container mx-auto max-w-4xl">
      <h3 className="text-3xl font-semibold mb-6">Currículum</h3>

      <a href="/cv_alejandro.pdf" download className="mb-4 inline-block bg-blue-600 text-white px-4 py-2 rounded-xl hover:bg-blue-700">
        Descargar PDF
      </a>

      <embed src="/cv_alejandro.pdf" type="application/pdf" className="w-full h-[600px] my-6" />

      <details className="mb-4">
        <summary className="text-lg font-bold cursor-pointer">Experiencia</summary>
        <p className="mt-2">Prácticas en Abalit como desarrollador Flutter, trabajando con APIs y metodologías ágiles SCRUM.</p>
      </details>

      <details className="mb-4">
        <summary className="text-lg font-bold cursor-pointer">Formación</summary>
        <p className="mt-2">Certificado IBM Data Analyst, Grado Superior en DAM, etc.</p>
      </details>

      <details>
        <summary className="text-lg font-bold cursor-pointer">Habilidades</summary>
        <ul className="mt-2 list-disc list-inside">
          <li>Python, SQL, Power BI, Excel</li>
          <li>Flutter, REST APIs, Git</li>
        </ul>
      </details>
    </section>
  );
}