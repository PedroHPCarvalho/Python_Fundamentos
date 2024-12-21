# Importa os módulos necessários para manipulação de arquivos e diretórios
import os  # Módulo para operações no sistema operacional, como criar, renomear e remover arquivos/diretórios
import shutil  # Módulo para operações avançadas de manipulação de arquivos/diretórios, como mover arquivos
from pathlib import Path  # Classe Path para manipulação de caminhos de arquivos/diretórios de forma multiplataforma

# Define o caminho raiz como o diretório pai do arquivo Python atual
ROOT_PATH = Path(__file__).parent

# Cria um novo diretório chamado "novo-directorio" no diretório raiz
os.mkdir(ROOT_PATH / "novo-directorio")

# Cria um novo arquivo vazio chamado "novo.txt" no diretório raiz
# O modo "w" abre o arquivo para escrita (e cria o arquivo se ele não existir)
arquivo = open(ROOT_PATH / "novo.txt", "w")
arquivo.close()  # Fecha o arquivo para liberar o recurso do sistema

# Renomeia o arquivo "novo.txt" para "alterado.txt"
os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# Remove (deleta) o arquivo "alterado.txt" do sistema de arquivos
os.remove(ROOT_PATH / "alterado.txt")

# Tenta mover o arquivo "novo.txt" para o diretório "novo-directorio" com um novo caminho
# Aqui, parece haver um erro, pois o arquivo "novo.txt" já foi renomeado ou removido nas linhas anteriores
shutil.move(ROOT_PATH / "novo.txt", ROOT_PATH / "novo-directorio" / "novo.txt")
