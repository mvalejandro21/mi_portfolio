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
    category = db.Column(db.String(50))
    
    # Descripción larga
    long_description = db.Column(db.Text)
    
    # Enlaces a documentación en Notion
    preprocessing_pdf = db.Column(db.String(500))
    analysis_pdf = db.Column(db.String(500))
    ml_pdf = db.Column(db.String(500))
    
    # Flags para secciones
    has_preprocessing = db.Column(db.Boolean, default=False)
    has_analysis = db.Column(db.Boolean, default=False)
    has_ml = db.Column(db.Boolean, default=False)
    
    # Enlaces adicionales según el tipo de proyecto
    dataset_url = db.Column(db.String(200))
    dashboard_url = db.Column(db.String(200))
    demo_url = db.Column(db.String(200))
    download_url = db.Column(db.String(200))
    
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
                image="wine_analysis.jpg",
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
                demo_url="https://winereviewalejandro.streamlit.app/",
                dataset_url="https://www.kaggle.com/datasets/zynicide/wine-reviews"
            ),
            cls(
                title="📊 Air BnB Analysis Barcelona",
                description="Analisis de precios y disponibilidad de alojamientos en Barcelona",
                image="sales_dashboard.jpg",
                github_url="https://github.com/tuusuario/sales-dashboard",
                live_url="https://tusuario-sales.streamlit.app",
                category="Data Visualization",
                tags="Python, Streamlit, Plotly, Pandas",
                analysis_pdf="analisis_airbnb.pdf",
                has_analysis=True,
                has_preprocessing=True,
                preprocessing_pdf="preprocesamiento_airbnb.pdf",
                dashboard_url="https://app.powerbi.com/reportEmbed?reportId=8c4b8471-6e14-47cc-bb48-71063bf202de&autoAuth=true&ctid=8aebddb6-3418-43a1-a255-b964186ecc64",
                download_url="/downloads/sales-report.pdf",
                dataset_url="https://insideairbnb.com/get-the-data"
            ),
            cls(
                title="🔍 Churn de clientes de IBM",
                description="Análisis de clusters para segmentación de clientes",
                image="segmentation.jpg",
                github_url="https://github.com/tuusuario/customer-segmentation",
                category="Data Analysis",
                tags="Python, Scikit-learn, Clustering, Visualización",
                preprocessing_pdf="https://your-notion.page.link/customer-preprocessing",
                analysis_pdf="https://your-notion.page.link/customer-analysis",
                has_preprocessing=True,
                has_analysis=True,
                download_url="/downloads/segmentation-report.pdf"
            )
        ]
        
        for project in predefined_projects:
            existing_project = cls.query.filter_by(title=project.title).first()
            if not existing_project:
                db_session.add(project)
                print(f"Proyecto agregado: {project.title}")
        
        db_session.commit()