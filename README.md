# Workshop-003

## Salome Rivas Marulanda - Código: 2242055

## Descripción del workshop:
Este taller integra Machine Learning con Data Streaming para desarrollar un sistema predictivo del índice de felicidad de diferentes países. Se utilizaron datos de felicidad mundial de los años 2015 a 2019, un modelo de Regresión Lineal y Apache Kafka para el streaming de datos en tiempo real.

### Estructura del workshop 

```
Workshop-003/
├── data/
│   ├── 2015.csv
│   ├── 2016.csv
│   ├── 2017.csv
│   ├── 2018.csv
│   ├── 2019.csv
│   └── df_clean.csv
├── notebooks/
│   ├── eda.ipynb
│   ├── training.ipynb
│   └── testing.ipynb
├── kafka/
│   ├── producer.py
│   └── consumer.py
├── models/
│   └── model.pkl
├── database/
│   └── predictions.db
├── evidence/
│   └── evidence1.png
│   └── evidence2.png
│   └── evidence3.png
│   └── evidence4.png
├── summary_report/
│   └── report.pdf
└── README.md
```

### Tecnologias usadas:

- **Python 3.14**
- **Apache Kafka 3.6.1**
- **Scikit-learn**
- **Pandas**
- **Matplotlib / Seaborn**
- **SQLite**


## Pasos para ejecutar este workshop 

### 1. Clona el repositorio

```bash
git clone https://github.com/Salo018/Workshop-003.git
cd Workshop-003
```

### 2. Instalar las dependencias 

```
pip install pandas scikit-learn matplotlib seaborn kafka-python sweetviz
```

### 3. Instalar Apache kafka 
```
https://kafka.apache.org/downloads
```

### 4. Instalar Java JDK en caso de que no lo tengas
```
https://www.oracle.com/java/technologies/downloads/
```
## Pasos para correr este workshop

### 1. Correr el EDA
Abre y ejecuta notebooks/eda.ipynb

### 2. Entrenar el modelo
Abre y ejecuta notebooks/training.ipynb

### 3. Levantar Kafka
Abre una terminal y ejecuta:
```
C:\kafka\bin\windows\kafka-server-start.bat C:\kafka\config\kraft\server.properties
```

### 4. Correr el Consumer
Abre una segunda terminal y ejecuta:
```
python kafka/consumer.py
```

### 5. Correr el Producer
Abre una tercera terminal y ejecuta:
```
python kafka/producer.py
```

### 6. Evaluar el modelo
Abre y ejecuta notebooks/testing.ipynb

## Decisiones clave 
- Se seleccionaron 4 features (GDP, Social Support, Life Expectancy y Freedom) con base en su correlación con el Happiness Score.
- Se usó Regresión Lineal por su simplicidad e interpretabilidad.
- Se usó SQLite como base de datos por ser ligera y no requiere instalación adicional.
- Kafka fue instalado manualmente en Windows debido a limitaciones de virtualización que me impedían usar Docker.
- El split de datos fue 70% entrenamiento y 30% prueba con random_state=80.