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
    
    # Nuevos campos
    long_description = db.Column(db.Text)
    documentation = db.Column(db.Text)
    dataset_url = db.Column(db.String(200))
    
    # Flags para secciones
    has_preprocessing = db.Column(db.Boolean, default=False)
    has_analysis = db.Column(db.Boolean, default=False)
    has_ml = db.Column(db.Boolean, default=False)
    
    # Contenido de las secciones
    preprocessing_content = db.Column(db.Text)
    analysis_content = db.Column(db.Text)
    ml_content = db.Column(db.Text)
    
    # Para el dashboard
    dashboard_path = db.Column(db.String(200))
    
    # Para la demo de ML
    demo_url = db.Column(db.String(200))
    
    def get_project_by_id(project_id):
        return Project.query.get_or_404(project_id)
    



wine_project = Project(
    title="🍷 Wine Variety Analysis",
    description="Análisis avanzado de vinos para identificar oportunidades de mercado y crear sistemas de recomendación",
    image="wine_analysis.jpg",
    github_url="https://github.com/tuusuario/wine-analysis",
    dataset_url="https://www.kaggle.com/datasets/zynicide/wine-reviews",
    category="Data Science",
    tags="Python, Pandas, NLP, spaCy, Machine Learning, Streamlit",
    long_description="""
    Proyecto completo de análisis de vinos que incluye:
    - Limpieza y preparación de datos
    - Análisis exploratorio avanzado
    - Extracción de sabores mediante NLP
    - Tres sistemas de recomendación diferentes
    - Identificación de vinos infravalorados
    """,
    documentation="""
    <h3>🏢 Contexto</h3>
    <p>Cliente: Empresa importadora de vinos</p>
    <p>Objetivo general: Optimizar el portafolio de vinos importados, identificando oportunidades de alto valor.</p>
    
    <h3>🔧 Proceso de Limpieza de Datos</h3>
    <ul>
        <li>Estandarización de columnas y tipos de datos</li>
        <li>Eliminación de duplicados y columnas innecesarias</li>
        <li>Tratamiento avanzado de valores nulos</li>
    </ul>
    
    <h3>🍷 Extracción de Sabores con NLP</h3>
    <p>Procesamiento de descripciones usando spaCy para identificar los 50 sabores/aromas más comunes.</p>
    """,
    has_preprocessing=True,
    has_analysis=True,
    has_ml=True,
    preprocessing_content="""
    <h2>Proceso Detallado de Limpieza de Datos</h2>
    
    <h3>📂 1. Dataset Original</h3>
    <p>Variables iniciales:</p>
    <ul>
        <li><strong>Geografía:</strong> country, province, region_1, region_2</li>
        <li><strong>Producto:</strong> variety, winery, designation</li>
        <li><strong>Valoración:</strong> points, price</li>
        <li><strong>Catador:</strong> taster_name, taster_twitter_handle</li>
        <li><strong>Sensorial:</strong> description</li>
    </ul>
    
    <h3>🧹 2. Limpieza General</h3>
    <p><strong>a. Estandarización:</strong></p>
    <ul>
        <li>Renombrado de columnas para consistencia</li>
        <li>Conversión de tipos de datos</li>
    </ul>
    
    <p><strong>b. Eliminación de duplicados:</strong> Se eliminaron entradas repetidas</p>
    
    <p><strong>c. Columnas eliminadas:</strong></p>
    <ul>
        <li>region_1, region_2 (demasiados nulos)</li>
        <li>designation (irrelevante para el análisis)</li>
        <li>taster_twitter_handle (sin valor analítico)</li>
    </ul>
    
    <h3>🧪 3. Tratamiento de Valores Nulos</h3>
    <p><strong>price:</strong></p>
    <ul>
        <li>Imputación por mediana agrupada por variety + province</li>
        <li>Para casos sin agrupación posible: mediana general</li>
    </ul>
    
    <p><strong>Otras columnas:</strong> Valores nulos restantes (&lt;0.6%) fueron eliminados</p>
    """,
    analysis_content="""
    <h2>Análisis Exploratorio de Datos</h2>
    
    <h3>❓ Preguntas Clave de Negocio</h3>
    
    <div class="analysis-question">
        <h4>📈 1. Relación calidad/precio</h4>
        <p>¿Qué países o regiones tienen los vinos con mejor puntuación ajustada al precio?</p>
        <div class="insight">
            <strong>Insight:</strong> "Los vinos portugueses y argentinos ofrecen una relación calidad/precio un 20% mejor que la media global."
        </div>
    </div>
    
    <div class="analysis-question">
        <h4>🗺️ 2. Zonas emergentes</h4>
        <p>¿Qué regiones menos conocidas tienen vinos muy bien puntuados?</p>
        <div class="insight">
            <strong>Insight:</strong> "Valle de Uco (Argentina) y Navarra (España) tienen vinos con 90+ puntos a mitad del precio de Burdeos."
        </div>
    </div>
    
    <div class="analysis-question">
        <h4>🍇 3. Variedad de uva</h4>
        <p>¿Qué variedades tienen más presencia global y qué puntuación media obtienen?</p>
        <div class="insight">
            <strong>Insight:</strong> "El Tempranillo fuera de España está obteniendo puntuaciones consistentes por debajo de los $20."
        </div>
    </div>
    
    <h3>📊 Dashboard Interactivo</h3>
    <p>Se desarrolló un dashboard en Power BI que permite explorar:</p>
    <ul>
        <li>Relaciones entre precio y puntuación</li>
        <li>Distribución geográfica de los mejores vinos</li>
        <li>Análisis comparativo por variedad</li>
    </ul>
    """,
    ml_content="""
    <h2>Sistemas de Recomendación de Vinos</h2>
    
    <div class="ml-project">
        <h3>🍷 Proyecto 1: Sommelier Virtual</h3>
        <p><strong>Recomendador basado en perfil de sabor del usuario</strong></p>
        
        <h4>🔧 Proceso</h4>
        <ul>
            <li>Extracción de sabores mediante NLP (spaCy)</li>
            <li>Creación de matriz de características sensoriales</li>
            <li>Motor de recomendación por similitud de coseno</li>
        </ul>
        
        <h4>🖥️ Interfaz (Streamlit)</h4>
        <p>Panel con sliders para ajustar preferencias sensoriales y visualización de resultados.</p>
    </div>
    
    <div class="ml-project">
        <h3>🍷 Proyecto 2: Sommelier AI</h3>
        <p><strong>Recomendador por vino similar</strong></p>
        
        <h4>🔧 Modelado</h4>
        <ul>
            <li>Algoritmo Nearest Neighbors (k=11)</li>
            <li>Distancia de coseno entre perfiles de sabor</li>
        </ul>
    </div>
    
    <div class="ml-project">
        <h3>🍷 Proyecto 3: Wine Value Analyzer</h3>
        <p><strong>Identificación de vinos infravalorados</strong></p>
        
        <h4>🔧 Modelado</h4>
        <ul>
            <li>Regresión lineal para predecir precio esperado</li>
            <li>Clasificación en 4 categorías de valor</li>
        </ul>
    </div>
    
    <div class="demo-section">
        <h3>🚀 Demo en Vivo</h3>
        <p>Puedes interactuar con el sistema de recomendación:</p>
        <a href="https://tusuariowine.streamlit.app" class="btn primary" target="_blank">
            <i class="fas fa-external-link-alt"></i> Probar Demo
        </a>
    </div>
    """,
    dashboard_path="wine_dashboard.pbix",
    demo_url="https://tusuariowine.streamlit.app"
)