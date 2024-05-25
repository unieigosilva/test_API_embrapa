# Adicionar o diretório raiz do projeto ao sys.path
import sys
sys.path.append('./app/')
import sys
import subprocess
import asyncio
from app.data_processing.database_update import update_database

# Função para instalar pywin32 no Windows
def install_pywin32():
    if sys.platform == "win32":
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pywin32==306"])
        except subprocess.CalledProcessError as e:
            print(f"Erro ao instalar pywin32: {e}")
            sys.exit(1)

if __name__ == "__main__":
    install_pywin32()
    asyncio.run(update_database())
    print("Para Iniciazar a API clicar http://127.0.0.1:8000 (Press CTRL+C to quit)")
    print("Para Verificação de  documentação da API clicar http://127.0.0.1:8000/docs (Press CTRL+C to quit)")
    print("Para gerar um tokem para API username: teste, password: teste ")