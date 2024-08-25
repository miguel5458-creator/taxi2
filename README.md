
Creación del Entorno Conda
Crea un entorno Conda llamado proyectogit con Python 3.12:

conda create --name proyectogit python=3.12

Activa el entorno proyectogit:

conda activate proyectogit



El archivo joblib esta alojado en google drive https://drive.google.com/drive/u/0/folders/12WYT8XNd3SnNbxOfVkNmszVXAWQCS678


![image](https://github.com/user-attachments/assets/cce5fe33-49f1-4a15-bcb5-6313680f2f3f)






Ejecute modal con el siguiente comando

modal deploy fastapi_app.py

![image](https://github.com/user-attachments/assets/ba7cb959-9481-40b6-992a-92f534daa4cd)



![image](https://github.com/user-attachments/assets/0c006b24-051f-498d-bc70-a2912349834b)

La url de la APP es 

https://miguel5458-creator--example-fastapi-app-fastapi-app.modal.run, el endpoit esta formado por la URL del archivo parquet:https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet

Puede probar la App desde el cmd con curl:

![image](https://github.com/user-attachments/assets/8685faa9-aad4-42a5-a58b-e8c049b2fbe7)


curl -X GET "https://miguel5458-creator--example-fastapi-app-fastapi-app.modal.run/process_url/?data_url=https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet"


Obteniendo las predicciones y el F1 Score:

![image](https://github.com/user-attachments/assets/56518166-57b8-496e-bdaa-a984649e3088)


Puede ejecutar localmente una intefaz grafica en Flask en backend app.py

 py app.py runserver

 ![image](https://github.com/user-attachments/assets/028eaf09-2f42-4338-955b-97ee2c463316)


 Coloque la url http://192.168.0.4:5000/ en el navegador y espere la redirección:

 
![image](https://github.com/user-attachments/assets/e7d03354-e887-447b-89b7-ee20ab82b5fd)

Luego coloque la url https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet obteniendo

![image](https://github.com/user-attachments/assets/0148457b-25cc-4d0d-96d7-765f803e2d9b)

El resultado es el mismo obtenido con el curl desde el cmd

![image](https://github.com/user-attachments/assets/d3028cdc-ddb6-496e-a388-016a090cd2d0)

![image](https://github.com/user-attachments/assets/a076d307-d1bc-424b-a237-d7baa222d57e)



Si no puede ejecutar el Archivo Flask vaya a la url https://eszk4xdkz57nssjbfwb3ow.streamlit.app/

![image](https://github.com/user-attachments/assets/a7712839-804c-45f0-bdb7-0430462e76fb)

y coloque la misma busqueda 

![image](https://github.com/user-attachments/assets/746f3dbe-ae6c-42b7-aa7e-d43f8b9fe4b2)


![image](https://github.com/user-attachments/assets/7001c9b7-9939-41c0-b494-18aded712162)
 Se obtiene el mismo json 

 En los 3 casos la ejecución es la misma el json se forma:

 1. predictions: Valores de las predicciones
 2. f1_score: Valor F1


