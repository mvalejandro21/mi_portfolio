from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory, flash
import os
from static.models.projects import db, Project  # Import del modelo y DB
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# BLOQUE PARA REINICIAR LA BASE DE DATOS 
# with app.app_context():
#     db.drop_all()  # Elimina todas las tablas (¡cuidado en producción!)
#     db.create_all() 

def init_database():
    """Crea las tablas si no existen y añade proyectos iniciales"""
    with app.app_context():
        db.create_all()
        # Inicializar los proyectos predefinidos
        Project.initialize_projects(db.session)
        print("Base de datos inicializada con proyectos")

# Llamar al inicio para que en Render la BD esté lista antes de la primera consulta
init_database()

@app.route("/projects")
def projects():
    all_projects = Project.get_all_projects()
    return render_template("projects.html", projects=all_projects)

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = Project.get_project_by_id(project_id)
    return render_template("project_detail.html", project=project)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                              'img/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    projects = Project.query.limit(3).all()
    return render_template('index.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/download_cv')
def download_cv():
    path = 'cv.pdf'
    return send_file(path, as_attachment=True)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route("/projects/<int:project_id>/documentation/<section>")
def project_documentation(project_id, section):
    project = Project.get_project_by_id(project_id)
    
    # Determinar qué PDF mostrar según la sección
    pdf_filename = None
    section_name = ""
    
    if section == "preprocessing" and project.has_preprocessing and project.preprocessing_pdf:
        pdf_filename = project.preprocessing_pdf
        section_name = "Preprocesamiento de Datos"
    elif section == "analysis" and project.has_analysis and project.analysis_pdf:
        pdf_filename = project.analysis_pdf
        section_name = "Análisis Exploratorio"
    elif section == "ml" and project.has_ml and project.ml_pdf:
        pdf_filename = project.ml_pdf
        section_name = "Machine Learning"
    
    if not pdf_filename:
        # Redirigir a la página de proyecto si no hay documento
        return redirect(url_for('project_detail', project_id=project_id))
    
    # Verificar si el archivo existe
    pdf_path = os.path.join('static', 'docs', 'pdf', pdf_filename)
    if not os.path.exists(pdf_path):
        return f"Archivo {pdf_filename} no encontrado en la carpeta static/docs/pdf/", 404
    
    return render_template('project_documentation.html', 
                         project=project, 
                         section=section,
                         section_name=section_name,
                         pdf_filename=pdf_filename)

@app.route('/view-pdf/<filename>')
def view_pdf(filename):
    # Ruta a la carpeta de PDFs
    pdf_path = os.path.join('static', 'docs', 'pdf', filename)
    if not os.path.exists(pdf_path):
        return f"PDF {filename} no encontrado en static/docs/pdf/", 404
        
    return send_file(pdf_path, mimetype='application/pdf')

@app.route('/download-pdf/<filename>')
def download_pdf(filename):
    # Ruta a la carpeta de PDFs
    pdf_path = os.path.join('static', 'docs', 'pdf', filename)
    if not os.path.exists(pdf_path):
        return f"PDF {filename} no encontrado en static/docs/pdf/", 404
        
    return send_file(pdf_path, as_attachment=True)

@app.route('/project/<int:project_id>/dashboard')
def project_dashboard(project_id):
    project = Project.get_project_by_id(project_id)
    return render_template('dashboard.html', project=project)

if __name__ == '__main__':
    init_database()
    app.run(debug=True)