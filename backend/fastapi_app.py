from fastapi import FastAPI, File, UploadFile
from modal import App, Image, asgi_app, Secret
from urllib.parse import unquote
import main2
import os

# Define the FastAPI app
web_app = FastAPI()
app = App("example-fastapi-app")

# Define the image for deployment, installing necessary libraries
# Define la imagen para el despliegue, incluyendo el archivo
image = (
    Image.debian_slim()
    .pip_install(
        "fastapi",
        "uvicorn",
        "pandas",
        "scikit-learn",
        "modal",
        "matplotlib",
        "seaborn",
        "requests",
        "pyarrow",  # Añadido para soporte de archivos Parquet
        "fastparquet"  # Alternativamente, si prefieres esta opción
    )
)

# Endpoint to process data from the URL
@web_app.get("/process_url/")
async def process_data_from_url(data_url: str):
    try:
        # Decodifica la URL para manejar caracteres especiales
        decoded_url = unquote(data_url)
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



# Set up the deployment details for the Modal platform
@app.function(image=image, secrets=[Secret.from_dotenv()])
@asgi_app()
def fastapi_app():
    return web_app

# Deploy the application if this script is run directly
if __name__ == "__main__":
    app.deploy("webapp")
