#Importar librerías necesarias
import json
import pickle
import sqlite3
import pandas as pd
from kafka import KafkaConsumer

# Cargar modelo entrenado
with open('C:/Users/Asus/OneDrive/Desktop/Workshop-003/models/model.pkl', 'rb') as f:
    model = pickle.load(f)

print("Modelo cargado exitosamente.")

# Conectar a base de datos SQLite
conn = sqlite3.connect('C:/Users/Asus/OneDrive/Desktop/Workshop-003/database/predictions.db')
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS predictions (
        record_id INTEGER,
        GDP REAL,
        Social_Support REAL,
        Life_Expectancy REAL,
        Freedom REAL,
        actual_score REAL,
        predicted_score REAL
    )
''')
conn.commit()

# Crear consumer
consumer = KafkaConsumer(
    'happiness-features',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8')),
    auto_offset_reset='earliest',
    group_id='happiness-group'
)

print("Esperando mensajes de Kafka...")

for mensaje in consumer:
    data = mensaje.value
    features = data['features']

    # Predecir
    X = pd.DataFrame([features])
    predicted_score = model.predict(X)[0]

    # Guardar en base de datos
    cursor.execute('''
        INSERT INTO predictions VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['record_id'],
        features['GDP'],
        features['Social_Support'],
        features['Life_Expectancy'],
        features['Freedom'],
        data['actual_score'],
        predicted_score
    ))
    conn.commit()

    print(f"  Registro {data['record_id']} → Real: {data['actual_score']:.3f} | Predicho: {predicted_score:.3f}")