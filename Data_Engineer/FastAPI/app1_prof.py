# 1. Importación de las bibliotecas
import uvicorn
from fastapi import FastAPI

# 2. Crear el objeto de la aplicación
app = FastAPI()

# 3. Ruta del índice, se abre automáticamente en http://127.0.0.1:8000
@app.get('/')
def index():
    '''
    Este es un docstring...
    '''
    return {'message': 'Hola, desconocido'}

# 4. Ruta con un único parámetro, devuelve el parámetro dentro de un mensaje
#    Ubicado en: http://127.0.0.1:8000/CualquierNombre
@app.get('/{name}')
def get_name(name: str):
    '''
    Este es el otro docstring...
    '''
    return {'message': f'Hola, {name}'}

# 5. Ejecutar la API con uvicorn
#    Se ejecutará en http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)