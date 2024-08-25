
from fastapi import FastAPI
from urllib.parse import unquote
from modal import Image, Stub, Secret
import uvicorn
import main2

# Define la aplicación FastAPI
fastapi_app = FastAPI()

@fastapi_app.get("/{path:path}")
async def process_data(path: str):
    try:
        decoded_url = unquote(path)
        result = main2.process_data_from_url(decoded_url)
        return {"status": "success", "result": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Define la imagen para el despliegue
image = (
    Image.debian_slim()
    .pip_install(
        "fastapi",
        "modal",
        "uvicorn",
        # Otras librerías necesarias
    )
)

# Configura el Stub para Modal
stub = Stub(image=image, secrets=[Secret.from_dotenv()])

# Configura la función de ejecución del servidor
@stub.function()
def run_server():
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)

# Despliega la aplicación si el script se ejecuta directamente
if __name__ == "__main__":
    stub.deploy("run_server")