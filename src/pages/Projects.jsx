import React from 'react';
import { Link } from 'react-router-dom';

const mockProjects = [
  { id: 'proyecto1', title: 'Análisis de Ventas', description: 'Proyecto de análisis exploratorio de datos de ventas.', image: '/img/proyecto1.png' },
  { id: 'proyecto2', title: 'Predicción de Clientes', description: 'Modelo de machine learning para predecir clientes.', image: '/img/proyecto2.png' },
];

export default function Projects() {
  return (
    <section className="py-20 px-6 container mx-auto">
      <h3 className="text-3xl font-semibold mb-8">Proyectos</h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {mockProjects.map(p => (
          <div key={p.id} className="border rounded-xl p-4 shadow-sm hover:shadow-md transition">
            <img src={p.image} alt={p.title} className="w-full h-48 object-cover rounded-lg mb-4" />
            <h4 className="text-xl font-bold mb-2">{p.title}</h4>
            <p className="text-gray-600 mb-3">{p.description}</p>
            <Link to={`/proyectos/${p.id}`} className="text-blue-600 underline">Ver más</Link>
          </div>
        ))}
      </div>
    </section>
  );
}