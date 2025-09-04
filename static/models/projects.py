from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    image = db.Column(db.String(100))
    github_url = db.Column(db.String(200))
    live_url = db.Column(db.String(200))
    tags = db.Column(db.String(200))
    category = db.Column(db.String(50))  # 'data-science', 'web-development', 'mobile', 'full-stack'
    project_type = db.Column(db.String(20))  # 'data', 'development', 'mixed'

    # Campos para todo tipo de proyectos
    long_description = db.Column(db.Text)
    technologies = db.Column(db.Text)  # Lista de tecnologías principales

    # Campos específicos para proyectos de datos
    has_preprocessing = db.Column(db.Boolean, default=False)
    has_analysis = db.Column(db.Boolean, default=False)
    has_ml = db.Column(db.Boolean, default=False)
    preprocessing_url = db.Column(db.String(500))
    analysis_url = db.Column(db.String(500))
    ml_url = db.Column(db.String(500))
    dataset_url = db.Column(db.String(200))
    dashboard_url = db.Column(db.String(200))

    # Campos específicos para proyectos de desarrollo
    has_frontend = db.Column(db.Boolean, default=False)
    has_backend = db.Column(db.Boolean, default=False)
    has_database = db.Column(db.Boolean, default=False)
    features = db.Column(db.Text)  # Lista de características principales

    # Campos generales
    demo_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    documentation_url = db.Column(db.String(200))
    
    def __repr__(self):
        return f'<Project {self.title}>'
    
    @classmethod
    def get_project_by_id(cls, project_id):
        return cls.query.get_or_404(project_id)
    
    @classmethod
    def get_all_projects(cls):
        return cls.query.all()
    
    @classmethod
    def initialize_projects(cls, db_session):
        predefined_projects = [
            cls(
                title="🍷 Wine Variety Analysis",
                description="Identificar oportunidades de mercado y crear sistemas de recomendación",
                image="wineproj.jpeg",
                github_url="https://github.com/tuusuario/wine-analysis",
                category="Data Science",
                tags="Python, Pandas, NLP, spaCy, Machine Learning, Streamlit",
                long_description="""
                Proyecto completo de análisis de vinos con enfoque en la identificación de oportunidades de mercado y la creación de sistemas de recomendación.
                Así como enfocarnos en temas económicos y exploración de los mismos.
                """,
                preprocessing_pdf="preprocesamiento_wine.pdf",
                analysis_pdf="analisis_wine.pdf", 
                ml_pdf="ml_wine.pdf",
                has_preprocessing=True,
                has_analysis=True,
                has_ml=True,
                project_type="data",
                technologies="Python, Pandas, NLP, spaCy, Scikit-learn, Streamlit",
                demo_url="https://winereviewalejandro.streamlit.app/",
                dataset_url="https://www.kaggle.com/datasets/zynicide/wine-reviews",
                dashboard_url="https://app.powerbi.com/reportEmbed?reportId=31978b18-5354-444e-8d69-bfaccc030d8c&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64"
            ),
            cls(
                title="📊 Air BnB Analysis Barcelona",
                description="Analisis de precios y disponibilidad de alojamientos en Barcelona",
                image="airbnbproj.jpeg",
                github_url="https://github.com/tuusuario/sales-dashboard",
                live_url="https://tusuario-sales.streamlit.app",
                category="Data Visualization",
                tags="Python, Streamlit, Plotly, Pandas",
                analysis_pdf="analisis_airbnb.pdf",
                has_analysis=True,
                project_type="data",
                long_description="""
                Proyecto de análisis de datos de AirBnB en Barcelona, centrado en la visualización de precios y disponibilidad de alojamientos.
                """,
                technologies="Python, Pandas, Streamlit, Plotly",
                has_preprocessing=True,
                preprocessing_pdf="preprocesamiento_airbnb.pdf",
                dashboard_url="https://app.powerbi.com/reportEmbed?reportId=8c4b8471-6e14-47cc-bb48-71063bf202de&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64",
                download_url="/downloads/sales-report.pdf",
                dataset_url="https://insideairbnb.com/get-the-data"
            ),
            cls(
                title="📊 CsharpProject",
                description="Análisis de datos de un proyecto en Csharp",
                image="csharpproj.jpeg",
                github_url="https://github.com/tuusuario/csharp-project",
                live_url="https://tusuario-csharp.streamlit.app",
                category=".NET Development",
                tags="Python, Streamlit, Plotly, Pandas",
                has_database=True,
                has_frontend=True,
                has_backend=True,
                project_type="data",
                long_description="""
                Proyecto de análisis de datos de un proyecto en Csharp.
                """,
                technologies="Python, Pandas, Streamlit, Plotly",
                has_preprocessing=True,
                preprocessing_pdf="preprocesamiento_airbnb.pdf",
                dashboard_url="https://app.powerbi.com/reportEmbed?reportId=8c4b8471-6e14-47cc-bb48-71063bf202de&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64",
                download_url="/downloads/sales-report.pdf",
                dataset_url="https://insideairbnb.com/get-the-data"
            )
        ]
        
        for project in predefined_projects:
            existing_project = cls.query.filter_by(title=project.title).first()
            if not existing_project:
                db_session.add(project)
                print(f"Proyecto agregado: {project.title}")
        
        db_session.commit()