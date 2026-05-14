# Workshop-003

## Salome Rivas Marulanda - Código: 2242055

## Descripción del proyecto:
Este proyecto integra Machine Learning con Data Streaming para desarrollar un sistema predictivo del índice de felicidad de diferentes países. Se utilizaron datos de felicidad mundial de los años 2015 a 2019, un modelo de Regresión Lineal y Apache Kafka para el streaming de datos en tiempo real.

### Estructura del proyecto 
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
├── /
└── README.md