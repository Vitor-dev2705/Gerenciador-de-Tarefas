from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status
import requests
from bs4 import BeautifulSoup

# Configurações do JWT
SECRET_KEY = "mysecretkey"  # Substitua por uma chave secreta segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Configuração do esquema OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Função para criar o token JWT
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Função para decodificar e validar o token JWT
def decode_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
# Função para buscar tarefas de uma fonte externa
def buscar_tarefas_externas():
    url = "https://www.google.com/"  # Exemplo de fonte pública com tarefas
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se a resposta HTTP foi bem-sucedida
        tarefas_externas = response.json()  # JSON da fonte externa
        return tarefas_externas[:10]  # Retorna apenas as 10 primeiras tarefas (exemplo)
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Erro ao buscar tarefas externas: {str(e)}")