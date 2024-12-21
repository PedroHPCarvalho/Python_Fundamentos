# Importa a classe Path do módulo pathlib para manipulação de caminhos de forma fácil e multiplataforma
from pathlib import Path

# Define o caminho raiz (ROOT_PATH) como o diretório pai do arquivo Python atual (__file__)
ROOT_PATH = Path(__file__).parent

# Tenta abrir um arquivo chamado "novo.txt" no diretório "novo-diretorio" dentro do caminho ROOT_PATH
try:
    # Usa o método "open" para tentar abrir o arquivo em modo leitura ("r")
    arquivo = open(ROOT_PATH / "novo-diretorio" / "novo.txt", "r")

# Captura o erro específico de arquivo não encontrado
except FileNotFoundError as exc:
    print("Arquivo não encontrado!")  # Mensagem informando que o arquivo não foi encontrado
    print(exc)  # Exibe a descrição detalhada do erro

# Captura o erro caso o caminho fornecido seja um diretório em vez de um arquivo
except IsADirectoryError as exc:
    print(f"Não foi possível abrir o arquivo: {exc}")  # Mensagem detalhada do erro

# Captura erros relacionados a operações de entrada/saída (IO), como permissões ou problemas no disco
except IOError as exc:
    print(f"Erro ao abrir o arquivo: {exc}")  # Mensagem informando o tipo de erro de IO

# Captura qualquer outro tipo de exceção que não esteja listado acima
except Exception as exc:
    print(f"Algum problema ocorreu ao tentar abrir o arquivo: {exc}")  # Mensagem genérica

# Comentário sobre outro bloco de código:
# Este bloco foi comentado, mas seria usado para lidar com erros ao tentar abrir um diretório como se fosse um arquivo
# try:
#     arquivo = open(ROOT_PATH / "novo-diretorio")  # Tenta abrir o diretório diretamente
# except IsADirectoryError as exc:  # Captura o erro de tentativa de abrir um diretório
#     print(f"Não foi possível abrir o arquivo: {exc}")  # Mensagem indicando o erro específico
