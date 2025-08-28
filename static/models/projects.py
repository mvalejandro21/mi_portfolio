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
    preprocessing_url = db.Column(db.String(500))
    analysis_url = db.Column(db.String(500))
    ml_url = db.Column(db.String(500))
    
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
                Proyecto completo de análisis de vinos que incluye documentación detallada
                en Notion sobre el proceso completo de data science.
                """,
                preprocessing_url="https://your-notion.page.link/data-preprocessing",
                analysis_url="https://your-notion.page.link/data-analysis", 
                ml_url="https://your-notion.page.link/machine-learning",
                has_preprocessing=True,
                has_analysis=True,
                has_ml=True,
                demo_url="https://tusuariowine.streamlit.app",
                dataset_url="https://www.kaggle.com/datasets/zynicide/wine-reviews"
            ),
            cls(
                title="📊 Sales Dashboard",
                description="Dashboard interactivo para análisis de ventas",
                image="sales_dashboard.jpg",
                github_url="https://github.com/tuusuario/sales-dashboard",
                live_url="https://tusuario-sales.streamlit.app",
                category="Data Visualization",
                tags="Python, Streamlit, Plotly, Pandas",
                analysis_url="https://your-notion.page.link/sales-analysis",
                has_analysis=True,
                dashboard_url="https://tusuario-sales.streamlit.app",
                download_url="/downloads/sales-report.pdf"
            ),
            cls(
                title="🔍 Customer Segmentation",
                description="Análisis de clusters para segmentación de clientes",
                image="segmentation.jpg",
                github_url="https://github.com/tuusuario/customer-segmentation",
                category="Data Analysis",
                tags="Python, Scikit-learn, Clustering, Visualization",
                preprocessing_url="https://your-notion.page.link/customer-preprocessing",
                analysis_url="https://your-notion.page.link/customer-analysis",
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