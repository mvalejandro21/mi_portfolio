from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
import os
from flask_sqlalchemy import SQLAlchemy
from src.static.models.projects import Project, db

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configura tu base de datos (ejemplo con SQLite, puedes cambiar a PostgreSQL/MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()
    # Si quieres insertar datos iniciales, puedes hacerlo aquí:
    if Project.query.count() == 0:
        db.session.add(Project(
            title="🍷 Wine Variety Analysis",
            description="Análisis avanzado de vinos...",
            image="wine_analysis.jpg",
            github_url="https://github.com/tuusuario/wine-analysis",
            dataset_url="https://www.kaggle.com/datasets/zynicide/wine-reviews",
            category="Data Science",
            tags="Python, Pandas, NLP, spaCy, Machine Learning, Streamlit",
            long_description="Proyecto completo de análisis...",
            documentation="Contenido HTML de documentación general",
            has_preprocessing=True,
            has_analysis=True,
            has_ml=True,
            preprocessing_content="Contenido HTML del preprocesamiento",
            analysis_content="Contenido HTML del análisis",
            ml_content="Contenido HTML del ML",
            dashboard_path="wine_dashboard.pbix",
            demo_url="https://tusuariowine.streamlit.app"
        ))
        db.session.commit()

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

@app.route('/projects')
def projects_page():
    projects = Project.query.all()  # Ahora viene del modelo
    return render_template('projects.html', projects=projects)

# Página de detalle del proyecto
@app.route('/projects/<int:project_id>')
def project_detail(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_detail.html', project=project)

# Subpáginas
@app.route('/projects/<int:project_id>/preprocessing')
def project_preprocessing(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_section.html', project=project, section_title="Preprocesamiento", content=project.preprocessing_content)

@app.route('/projects/<int:project_id>/analysis')
def project_analysis(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_section.html', project=project, section_title="Análisis", content=project.analysis_content)

@app.route('/projects/<int:project_id>/ml')
def project_ml(project_id):
    project = Project.query.get_or_404(project_id)
    return render_template('project_section.html', project=project, section_title="Machine Learning", content=project.ml_content)

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
    app.run(debug=True)
