from pathlib import Path  # Importa a classe Path para manipulação de caminhos

# Define o caminho raiz como o diretório onde o script está localizado
ROOT_PATH = Path(__file__).parent

# Tentativa de abrir o arquivo "fileTest1" no modo de leitura ("r")
try:
    with open(ROOT_PATH / "fileTest1", "r") as arquivo:
        # Lê todo o conteúdo do arquivo e o exibe no console
        print(arquivo.read())
except IOError as exc:
    # Captura erros de entrada/saída (como arquivo inexistente ou permissão negada)
    print(f"Erro ao abrir o arquivo {exc}")

# Tentativa de abrir o arquivo "fileTest1" no modo de escrita ("w")
try:
    with open(ROOT_PATH / "fileTest1", "w", encoding="utf-8") as arquivo:
        # Escreve o texto no arquivo. Caso o arquivo não exista, ele será criado
        arquivo.write("Aprendendo manipular arquivos")
except IOError as exc:
    # Captura erros ao tentar abrir ou escrever no arquivo
    print(f"Erro ao abrir arquivo {exc}")
