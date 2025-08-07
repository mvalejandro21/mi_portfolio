import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <section className="flex flex-col items-center justify-center text-center py-32 px-6 bg-gray-50">
      <h2 className="text-4xl font-bold mb-4">Hola, soy Alejandro</h2>
      <p className="text-lg mb-6 max-w-2xl">
        Data Analyst y desarrollador. Transformo datos en decisiones y creo soluciones digitales con impacto.
      </p>
      <a href="/cv_alejandro.pdf" download className="bg-blue-600 text-white px-6 py-3 rounded-xl hover:bg-blue-700 transition">
        Descargar CV
      </a>
      <Link to="/proyectos" className="mt-4 underline text-blue-600">Ver mis proyectos</Link>
    </section>
  );
}
