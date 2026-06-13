# Usar a imagem oficial do Python
FROM python:3.9-slim

# Definir a pasta de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo de dependências e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código do projeto para dentro do container
COPY . .

# Liberar a porta 5000 (usada pelo Flask)
EXPOSE 5000

# Comando para rodar o site
CMD ["python", "app.py"]