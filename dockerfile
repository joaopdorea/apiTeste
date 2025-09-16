FROM python:3.13.3

# Instala o Poetry
RUN pip install poetry

# Copia os arquivos do projeto
COPY . /src
WORKDIR /src

# Instala dependências (sem instalar o próprio pacote)
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Render expõe a porta via variável $PORT (default 10000)
EXPOSE 10000

# Inicia a API com uvicorn
ENTRYPOINT ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "10000"]