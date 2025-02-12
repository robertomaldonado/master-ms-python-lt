FROM python:3.13-slim-bullseye

ENV PORT="8000"
ENV CORES="2"
ENV SERVICE_NAME="users"

RUN apt-get update && \
    apt-get install -y gcc openssl libpq-dev

# creates requirements.txt

WORKDIR /app

COPY . /app

RUN pip install uv
RUN uv pip compile pyproject.toml -o requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto que FastAPI usará
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["sh", "/app/scripts/start.sh"]
