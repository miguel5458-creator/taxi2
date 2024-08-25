# main2.py
import os
import pandas as pd
from datetime import datetime

from src import load_data, preprocess, train_model, save_model, load_model, predict, evaluate, visualize_results

def obtener_ruta_del_script():
    ruta_absoluta = os.path.abspath(__file__)
    directorio_del_script = os.path.dirname(ruta_absoluta)
    return directorio_del_script

def process_data_from_url(data_url):
    ruta = obtener_ruta_del_script()
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> Iniciando proceso\n")

    target_col = "high_tip"

    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> cargando modelo para evaluar datos\n")
    model = load_model(f"{ruta}\\models\\random_forest.joblib")
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> modelo cargado\n")

    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> cargando datos\n")
    taxi_test = load_data(data_url)
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> preprocesando datos\n")
    taxi_test = preprocess(taxi_test, target_col)
    X_test = taxi_test[['pickup_weekday', 'pickup_hour', 'work_hours', 'pickup_minute', 'passenger_count', 'trip_distance', 'trip_time', 'trip_speed', 'PULocationID', 'DOLocationID', 'RatecodeID']]
    y_test = taxi_test[target_col]
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> test\n")
    preds = predict(model, X_test)

    # Mostrar solo una muestra de las predicciones para evitar problemas de memoria
    sample_preds = preds[:100]  # Muestra los primeros 100 elementos
    print(f"Sample predictions: {sample_preds}\n")

    f1_score = evaluate(y_test, preds)
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> F1: {f1_score}\n")
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> proceso finalizado\n")

    return {
        "predictions": list(sample_preds),  # Devuelve solo la muestra
        "f1_score": f1_score
    }

