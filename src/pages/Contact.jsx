import React from 'react';

export default function Contact() {
  return (
    <section className="py-20 px-6 container mx-auto max-w-xl">
      <h3 className="text-3xl font-semibold mb-6">Contacto</h3>
      <p className="mb-4">
        Puedes escribirme a <a href="mailto:tuemail@gmail.com" className="text-blue-600">tuemail@gmail.com</a> o rellenar este formulario:
      </p>
      <form className="grid gap-4">
        <input type="text" placeholder="Nombre" className="border p-2 rounded" />
        <input type="email" placeholder="Email" className="border p-2 rounded" />
        <textarea placeholder="Mensaje" className="border p-2 rounded h-32" />
        <button type="submit" className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700">Enviar</button>
      </form>
    </section>
  );
}
