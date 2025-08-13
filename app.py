from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
import os
import json
from src.static.models.projects import Project

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Cargar datos de proyectos desde JSON
with open('projects.json', 'r') as f:
    projects = json.load(f)




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                              'img/favicon.ico', mimetype='image/vnd.microsoft.icon')
@app.route('/')
def home():
    return render_template('index.html', projects=projects[:3])

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/cv')
def cv():
    return render_template('cv.html')

@app.route('/download_cv')
def download_cv():
    # Ruta al archivo CV (asegúrate de tener un archivo llamado 'cv.pdf' en la raíz)
    path = 'cv.pdf'
    return send_file(path, as_attachment=True)

@app.route('/projects')
def projects_page():
    return render_template('projects.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    # Si usas SQLAlchemy
    project = Project.query.get_or_404(project_id)
    
    # Si usas el JSON (como en tu código original)
    # project = next((p for p in projects if p['id'] == project_id), None)
    
    if not project:
        return redirect(url_for('projects_page'))
    
    # Convertir el objeto SQLAlchemy a dict si es necesario
    project_dict = {
        'id': project.id,
        'title': project.title,
        'description': project.description,
        'image': project.image,
        'github_url': project.github_url,
        'live_url': project.live_url,
        'tags': project.tags,
        'category': project.category,
        'long_description': project.long_description,
        'documentation': project.documentation,
        'dataset_url': project.dataset_url,
        'has_preprocessing': project.has_preprocessing,
        'has_analysis': project.has_analysis,
        'has_ml': project.has_ml,
        'preprocessing_content': project.preprocessing_content,
        'analysis_content': project.analysis_content,
        'ml_content': project.ml_content,
        'dashboard_path': project.dashboard_path,
        'demo_url': project.demo_url
    }
    
    return render_template('project_detail.html', project=project_dict)

@app.route('/project/<int:project_id>/<subpage>')
def project_subpage(project_id, subpage):
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project or subpage not in ['documentacion', 'preprocesamiento', 'analisis', 'ml']:
        return redirect(url_for('project_detail', project_id=project_id))
    
    content = project.get(subpage, '')
    title = subpage.capitalize()
    
    return render_template('project_subpage.html', project=project, title=title, content=content)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form.get('subject', '')
        message = request.form['message']
        # Aquí pondrías la lógica para enviar correo, por ahora simplemente redirigimos con éxito
        return redirect(url_for('contact_success'))
    return render_template('contact.html', success=False)

@app.route('/contact/success')
def contact_success():
    return render_template('contact.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)
