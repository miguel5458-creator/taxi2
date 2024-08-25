from flask import Flask, request, render_template, jsonify
from urllib.parse import quote
import sys
import os
import requests

# Agrega el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import main2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_data():
    try:
        data_url = request.form['data_url']
        # Codifica la URL para evitar problemas con caracteres especiales
        encoded_url = quote(data_url, safe='')

        # Llamar al endpoint de FastAPI
        fastapi_url = f"https://miguel5458-creator--example-fastapi-app-fastapi-app-dev.modal.run/process_url/?data_url={encoded_url}"
        response = requests.get(fastapi_url)
        response.raise_for_status()  # Asegúrate de que la solicitud fue exitosa
        response_data = response.json()

        # Maneja la respuesta de FastAPI
        if response_data["status"] == "success":
            return jsonify({
                "status": "success",
                "result": response_data["result"]
            })
        else:
            raise ValueError(response_data["message"])

    except requests.RequestException as e:
        # Maneja errores relacionados con la solicitud HTTP
        return jsonify({
            "status": "error",
            "message": f"Error al realizar la solicitud a FastAPI: {str(e)}"
        })
    except ValueError as e:
        # Maneja errores específicos de los datos
        return jsonify({
            "status": "error",
            "message": str(e)
        })
    except Exception as e:
        # Maneja cualquier otro error
        return jsonify({
            "status": "error",
            "message": str(e)
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)