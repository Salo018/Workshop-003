#Importar librerías necesarias
import json
import time
import pandas as pd
from kafka import KafkaProducer
from sklearn.model_selection import train_test_split

# Cargar dataset limpio
df = pd.read_csv('C:/Users/Asus/OneDrive/Desktop/Workshop-003/data/df_clean.csv')

# Separar features y target
X = df[['GDP', 'Social_Support', 'Life_Expectancy', 'Freedom']]
y = df['Happiness_Score']

# Mismo split que en training (random_state=42 para que sea el mismo 30%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print(f"Enviando {len(X_test)} registros de prueba a Kafka...")

for i in range(len(X_test)):
    mensaje = {
        'record_id': i,
        'features': {
            'GDP': float(X_test.iloc[i]['GDP']),
            'Social_Support': float(X_test.iloc[i]['Social_Support']),
            'Life_Expectancy': float(X_test.iloc[i]['Life_Expectancy']),
            'Freedom': float(X_test.iloc[i]['Freedom'])
        },
        'actual_score': float(y_test.iloc[i])
    }
    producer.send('happiness-features', value=mensaje)
    print(f"  → Registro {i+1}/{len(X_test)}", end='\r')
    time.sleep(0.05)

producer.flush()
producer.close()
print(f"\n{len(X_test)} registros enviados exitosamente.")