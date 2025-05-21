# Social Media vs Productivity - Data Analysis

Este proyecto analiza la relación entre el uso de redes sociales y la productividad laboral. Está organizado en módulos separados para la carga, limpieza y análisis de datos, con pruebas unitarias y medición de cobertura de código.

## Origen del dataset

El dataset utilizado proviene de Kaggle y se titula **"[Social Media Usage vs Productivity](https://www.kaggle.com/datasets/mahdimashayekhi/social-media-vs-productivity)"**. Fue publicado por el usuario Mahdi Mashayekhi y contiene respuestas de una encuesta relacionada con:

- Tiempo de uso de redes sociales
- Productividad percibida y real
- Estilo de trabajo
- Estrés, sueño y hábitos digitales

El archivo original en formato CSV debe guardarse en el directorio `data/` bajo el nombre:

```

data/social\_media\_vs\_productivity.csv

```

## Estructura del proyecto

```

data-analisys-real/
├── data/
│   └── social\_media\_vs\_productivity.csv
├── outputs/
│   └── analysis\_summary.txt
├── src/
│   ├── **init**.py
│   ├── load\_data.py
│   ├── process\_data.py
│   └── analysis.py
├── tests/
│   ├── test\_load\_data.py
│   ├── test\_process\_data.py
│   └── test\_analysis.py
├── htmlcov/
│   └── index.html
├── README.md
└── requirements.txt

````

## Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/tu-usuario/data-analisys-real.git
cd data-analisys-real
````

2. Crea un entorno virtual e instala dependencias:

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

1. Ejecuta el flujo de análisis completo:

```bash
python src/load_data.py
python src/process_data.py
python src/analysis.py
```

2. El resumen del análisis se guarda en:

```
outputs/analysis_summary.txt
```

## Pruebas y cobertura

Ejecuta los tests y genera un reporte de cobertura:

```bash
PYTHONPATH=$(pwd) pytest --cov=src --cov-report=term-missing --cov-report=html
```

Abre el archivo `htmlcov/index.html` en tu navegador para ver el informe visual.

## Contenido del análisis

* Estadísticas descriptivas de variables numéricas.
* Correlaciones con el puntaje de productividad real.
* Promedios agrupados por tipo de trabajo.
* Visualizaciones de regresión (opcional en notebooks o scripts).

## Requisitos

* Python 3.8+
* pandas
* seaborn
* matplotlib
* pytest
* pytest-cov

## Autora 
Juliana Briceño Castro

## Licencia

MIT


