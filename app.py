from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
import os
from static.models.projects import db, Project  # Import del modelo y DB

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form.get('subject', '')
        message = request.form['message']
        return redirect(url_for('contact_success'))
    return render_template('contact.html', success=False)

@app.route('/contact/success')
def contact_success():
    return render_template('contact.html', success=True)

@app.route("/projects/<int:project_id>/documentation/<section>")
def project_documentation(project_id, section):
    project = Project.get_project_by_id(project_id)
    
    # Determinar qué URL de documento usar según la sección
    pdf_url = None
    if section == "preprocessing" and project.has_preprocessing:
        pdf_url = project.preprocessing_url
    elif section == "analysis" and project.has_analysis:
        pdf_url = project.analysis_url
    elif section == "ml" and project.has_ml:
        pdf_url = project.ml_url
    
    if not pdf_url:
        # Redirigir a la página de proyecto si no hay documento
        return redirect(url_for('project_detail', project_id=project_id))
    
    # Extraer el nombre del archivo de la URL
    filename = pdf_url.split('/')[-1]
    
    return render_template('project_documentation.html', 
                         project=project, 
                         section=section,
                         pdf_url=pdf_url,
                         filename=filename)

@app.route('/download-pdf/<path:filename>')
def download_pdf(filename):
    # Asumiendo que los PDFs están en la carpeta static/docs/
    return send_from_directory('static/docs', filename, as_attachment=True)

if __name__ == '__main__':
    init_database()
    app.run(debug=True)