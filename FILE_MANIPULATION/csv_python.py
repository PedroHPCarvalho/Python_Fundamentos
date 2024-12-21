# Importa os módulos necessários
import csv  # Módulo para trabalhar com arquivos CSV
from pathlib import Path  # Classe para manipulação de caminhos de arquivos/diretórios

# Define o caminho raiz como o diretório pai do arquivo Python atual
ROOT_PATH = Path(__file__).parent

# Constantes que representam os índices das colunas no arquivo CSV
COLUNA_ID = 0  # Índice da coluna "id"
COLUNA_NOME = 1  # Índice da coluna "nome"

# Tentativa de criar e escrever no arquivo CSV
try:
    # Abre o arquivo "usuarios.csv" no modo de escrita ("w")
    # O argumento `newline=""` previne linhas em branco extras em sistemas Windows
    # O argumento `encoding="utf-8"` assegura a compatibilidade com caracteres especiais
    with open(ROOT_PATH / "usuarios.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)  # Cria um objeto escritor para o arquivo CSV
        escritor.writerow(["id", "nome"])  # Escreve a linha de cabeçalho no CSV
        escritor.writerow(["1", "Maria"])  # Adiciona a primeira linha de dados
        escritor.writerow(["2", "João"])  # Adiciona a segunda linha de dados
except IOError as exc:
    # Captura erros de entrada/saída ao tentar criar ou escrever no arquivo
    print(f"Erro ao criar o arquivo. {exc}")

# Tentativa de ler o arquivo CSV usando um leitor comum
try:
    # Abre o arquivo "usuarios.csv" no modo de leitura ("r")
    with open(ROOT_PATH / "usuarios.csv", "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)  # Cria um objeto leitor para o arquivo CSV
        for idx, row in enumerate(leitor):  # Itera sobre as linhas do arquivo
            if idx == 0:
                # Pula a primeira linha (cabeçalho)
                continue
            # Imprime os dados das colunas "id" e "nome"
            print(f"ID: {row[COLUNA_ID]}")
            print(f"Nome: {row[COLUNA_NOME]}")
except IOError as exc:
    # Captura erros de entrada/saída ao tentar ler o arquivo
    print(f"Erro ao criar o arquivo. {exc}")

# Tentativa de ler o arquivo CSV usando um leitor baseado em dicionário
try:
    # Abre o arquivo "usuarios.csv" no modo de leitura
    with open(ROOT_PATH / "usuarios.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)  # Cria um objeto leitor que usa o cabeçalho como chave
        for row in reader:  # Itera sobre as linhas do arquivo como dicionários
            # Imprime os valores das colunas "id" e "nome" usando as chaves do dicionário
            print(f"ID: {row['id']}")
            print(f"Nome: {row['nome']}")
except IOError as exc:
    # Captura erros de entrada/saída ao tentar ler o arquivo
    print(f"Erro ao criar o arquivo. {exc}")
