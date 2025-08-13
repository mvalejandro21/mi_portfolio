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
    """Crea las tablas si no existen y añade datos iniciales."""
    with app.app_context():
        db.create_all()
        
        # Verificar si ya existen proyectos para no duplicar
        if Project.query.count() == 0:
            wine_project = Project(
                title="🍷 Wine Variety Analysis",
                description="Análisis avanzado de vinos para identificar oportunidades de mercado...",
                image="wine_analysis.jpg",
                github_url="https://github.com/tuusuario/wine-analysis",
                # Añade aquí todos los campos necesarios
            )
            db.session.add(wine_project)
            db.session.commit()
            print("✅ Proyecto de ejemplo añadido a la base de datos.")
        else:
            print("✅ Base de datos ya contiene datos.")
# Llamar al inicio para que en Render la BD esté lista antes de la primera consulta
init_database()

@app.route("/projects")
def projects():
    all_projects = Project.query.all()
    return render_template("projects.html", projects=all_projects)

@app.route("/projects/<int:project_id>")
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
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

if __name__ == '__main__':
    init_database()
    app.run(debug=True)
