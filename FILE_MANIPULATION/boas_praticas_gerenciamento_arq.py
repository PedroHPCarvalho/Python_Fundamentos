from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
  with open(ROOT_PATH / "fileTest1" , "r") as arquivo:
    print(arquivo.read())
except IOError as exc:
  print(f"Erro ao abrir o arquivo {exc}")

try:
  with open(ROOT_PATH / "fileTest1" , "w", encoding="utf-8") as arquivo:
    arquivo.write("Aprendendo manipular arquivos")
except IOError as exc:
  print(f"Erro ao abrir arquivo {exc}")