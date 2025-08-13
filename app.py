from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
import os
from static.models.projects import db, Project  # Import del modelo

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configura tu base de datos (ejemplo con SQLite, puedes cambiar a PostgreSQL/MySQL)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

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
    with app.app_context():
        db.create_all()
    app.run(debug=True)
