from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import requests

app = FastAPI()

# Configuración de seguridad
security = HTTPBearer()

# Dependencia para obtener el rol actual basado en el token de acceso
def get_current_role(auth: HTTPAuthorizationCredentials = Depends(security)):
    token = auth.credentials
    # Verificar el token y extraer el rol
    if token == 'admin':
        return 'admin'
    elif token == 'user':
        return 'user'
    else:
        raise HTTPException(status_code=401, detail='Token inválido')

# Ruta de inicio de sesión
@app.post('/login')
def login(credentials: HTTPAuthorizationCredentials):
    # Verificar las credenciales de inicio de sesión (ejemplo simplificado)
    if credentials.username == 'admin' and credentials.password == 'admin123':
        return {'access_token': 'admin', 'token_type': 'bearer', 'role': 'admin'}
    elif credentials.username == 'user' and credentials.password == 'user123':
        return {'access_token': 'user', 'token_type': 'bearer', 'role': 'user'}
    else:
        raise HTTPException(status_code=401, detail='Credenciales inválidas')

# Ruta protegida por roles
@app.get('/dashboard')
def dashboard(role: str = Depends(get_current_role)):
    if role == 'admin':
        # Llamar a la API para usuarios administradores
        response = requests.get('http://localhost:8000/tarjetas')
        data = response.json()
        return {'message': 'Panel de administrador', 'data': data}
    elif role == 'user':
        # Llamar a la API para usuarios regulares
        response = requests.get('http://localhost:8000/users')
        data = response.json()
        return {'message': 'Panel de usuario', 'data': data}
    else:
        raise HTTPException(status_code=403, detail='Acceso no autorizado')


if __name__ == "__auth__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)