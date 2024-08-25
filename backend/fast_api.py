from fastapi import FastAPI
from urllib.parse import unquote
from modal import App, Image, asgi_app, Secret
import main2  # Asegúrate de que main2.py esté en el mismo directorio o en el PYTHONPATH

# Define la aplicación FastAPI
app = FastAPI()

# Define la ruta para procesar datos
@app.get("/{path:path}")
async def process_data(path: str):
    try:
        # Decodifica la URL para manejar caracteres especiales
        decoded_url = unquote(path)
        result = main2.process_data_from_url(decoded_url)
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }

# Define la imagen para el despliegue, instalando las bibliotecas necesarias
image = (
    Image.debian_slim()
    .pip_install(
        "fastapi",
        "modal",
        "uvicorn",
    )
)

# Configura el despliegue en Modal
app_modal = App("example-fastapi-app", image=image, secrets=[Secret.from_dotenv()])

@app_modal.function()
@asgi_app()
def fastapi_app():
    return app

# Despliega la aplicación si se ejecuta este script directamente
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

