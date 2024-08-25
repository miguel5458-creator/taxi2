import os
import pandas as pd
from datetime import datetime
import requests
from joblib import load
from src import load_data, preprocess, predict, evaluate

def obtener_ruta_del_script():
    ruta_absoluta = os.path.abspath(__file__)
    directorio_del_script = os.path.dirname(ruta_absoluta)
    return directorio_del_script

def download_file_from_google_drive(file_id, destination):
    URL = f"https://drive.google.com/uc?id={file_id}"
    try:
        response = requests.get(URL, stream=True)
        response.raise_for_status()  # Verifica que la solicitud haya tenido éxito
        with open(destination, 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
    except requests.RequestException as e:
        raise Exception(f"Error downloading file: {e}")

def process_data_from_url(data_url):
    ruta = obtener_ruta_del_script()
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> Iniciando proceso\n")

    target_col = "high_tip"
    model_path = os.path.join(ruta, "random_forest.joblib")

    # Descargar el archivo del modelo desde Google Drive
    file_id = "1CVsEcUrq6X_MtH1OvoCTYXyjL7EiIi_y"
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> descargando modelo\n")
    try:
        download_file_from_google_drive(file_id, model_path)
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> modelo descargado\n")
    except Exception as e:
        print(f"Error downloading model: {e}")
        return {"status": "error", "message": str(e)}

    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> cargando modelo\n")
    try:
        model = load(model_path)
        print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> modelo cargado\n")
    except Exception as e:
        print(f"Error loading model: {e}")
        return {"status": "error", "message": str(e)}

    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} -> cargando datos\n")
    try:
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
    except Exception as e:
        print(f"Error processing data: {e}")
        return {"status": "error", "message": str(e)}
