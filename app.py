from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
import os
import json

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
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project:
        return redirect(url_for('projects_page'))
    return render_template('project_detail.html', project=project)

@app.route('/proyecto/<int:project_id>/<subpage>')
def project_subpage(project_id, subpage):
    project = next((p for p in projects_data if p['id'] == project_id), None)
    if not project:
        abort(404)
    
    # Determinar el título basado en la subpágina
    titles = {
        'preprocesamiento': 'Preprocesamiento',
        'analisis': 'Análisis',
        'ml': 'Machine Learning'
    }
    title = titles.get(subpage, 'Proyecto')
    
    # Obtener el contenido correcto
    content_key = {
        'preprocesamiento': 'preprocesamiento',
        'analisis': 'analisis',
        'ml': 'ml'
    }.get(subpage)
    
    content = project.get(content_key, 'Contenido no disponible')
    
    return render_template('project_subpage.html', 
                         project=project,
                         title=title,
                         subpage=subpage,  # Asegúrate de pasar esto
                         content=content)

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
