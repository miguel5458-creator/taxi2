from fastapi import FastAPI
import uvicorn
import main2  # Asegúrate de que main2.py esté en el mismo directorio o en el PYTHONPATH
from urllib.parse import unquote

app = FastAPI()

@app.get("/{path:path}")
def process_data(path: str):
    try:
        # Decodifica la URL para manejar caracteres especiales
        decoded_url = unquote(path)
        print(f"Decoding URL: {decoded_url}")  # Verifica la URL decodificada
        result = main2.process_data_from_url(decoded_url)
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        print(f"Error: {e}")  # Imprime el error para diagnóstico
        return {
            "status": "error",
            "message": str(e)
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)