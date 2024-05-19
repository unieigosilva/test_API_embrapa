# Use uma imagem base do Python 3.10
FROM python:3.10-slim

# Instale as dependências do sistema e o Rust
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    gcc \
    libffi-dev \
    libssl-dev \
    cargo \
    && curl https://sh.rustup.rs -sSf | sh -s -- -y \
    && apt-get clean

# Adicione Rust e Cargo ao PATH
ENV PATH="/root/.cargo/bin:${PATH}"

# Atualize o pip
RUN pip install --upgrade pip

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o arquivo de requisitos e constraints e instale as dependências
COPY ../requirements.txt /app/requirements.txt
COPY Docker/constraints.txt /app/constraints.txt

# Mostre o conteúdo dos arquivos para depuração
RUN cat /app/requirements.txt
RUN cat /app/constraints.txt

# Instale as dependências com constraints
RUN pip install --no-cache-dir -r /app/requirements.txt -c /app/constraints.txt

# Copie o restante do código da aplicação para o contêiner
COPY ../ /app

# Exponha a porta em que a aplicação será executada
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
