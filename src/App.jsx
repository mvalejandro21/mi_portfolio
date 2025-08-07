import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// Import pages
import Home from "./pages/Home";
import About from "./pages/About";
import Projects from "./pages/Projects";
import CV from "./pages/CV";
import Contact from "./pages/Contact";
import ProjectDetail from "./pages/ProjectDetail";

export default function App() {
  return (
    <Router>
      <div className="min-h-screen bg-neutral-light text-primary font-sans">
        <header className="sticky top-0 z-50 bg-white/80 backdrop-blur-md shadow-md">
          <nav className="container mx-auto flex justify-between items-center py-4 px-6">
            <h1 className="text-xl font-bold tracking-tight">Alejandro</h1>
            <ul className="flex gap-6 text-sm font-medium">
              <li><Link to="/" className="hover:text-accent transition-colors">Inicio</Link></li>
              <li><Link to="/proyectos" className="hover:text-accent transition-colors">Proyectos</Link></li>
              <li><Link to="/cv" className="hover:text-accent transition-colors">CV</Link></li>
              <li><Link to="/sobremi" className="hover:text-accent transition-colors">Sobre mí</Link></li>
              <li><Link to="/contacto" className="hover:text-accent transition-colors">Contacto</Link></li>
            </ul>
          </nav>
        </header>

        <main className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/proyectos" element={<Projects />} />
            <Route path="/proyectos/:id" element={<ProjectDetail />} />
            <Route path="/cv" element={<CV />} />
            <Route path="/sobremi" element={<About />} />
            <Route path="/contacto" element={<Contact />} />
          </Routes>
        </main>

        <footer className="text-center py-6 text-sm text-gray-500 bg-neutral">
          © {new Date().getFullYear()} Alejandro — Todos los derechos reservados.
        </footer>
      </div>
    </Router>
  );
}
