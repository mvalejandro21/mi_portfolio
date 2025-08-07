from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import json

app = Flask(__name__)

# Cargar datos de proyectos desde JSON
with open('projects.json', 'r') as f:
    projects = json.load(f)

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

@app.route('/project/<int:project_id>/<subpage>')
def project_subpage(project_id, subpage):
    project = next((p for p in projects if p['id'] == project_id), None)
    if not project or subpage not in ['documentacion', 'preprocesamiento', 'analisis', 'ml']:
        return redirect(url_for('project_detail', project_id=project_id))
    
    # Contenido específico para cada subpágina
    content = project[subpage]
    title = subpage.capitalize()
    
    return render_template('project_subpage.html', project=project, title=title, content=content)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí iría la lógica para enviar el correo
        return redirect(url_for('contact_success'))
    return render_template('contact.html')

@app.route('/contact/success')
def contact_success():
    return render_template('contact.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)