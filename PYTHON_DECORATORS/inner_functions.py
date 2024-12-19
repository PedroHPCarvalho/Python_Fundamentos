#Neste Exemplo vamos rever o conceito de inner functions, que seria ter funcoes declaradas dentro do escopo de uma funcao

def principal():
  print("Executar a função principal")

  def funcao_protocolo1():
    print("executando o protocolo")

  def funcao_finalizacao(nome_protocolo):
    print(f"executando o protocolo de finalizacao {nome_protocolo}")

  funcao_protocolo1()
  funcao_finalizacao("Encerrando Testes")


principal()
print()
#Essas funçoes não existem no escopo global, ou fora da funcao onde foram declarados
# funcao_protocolo1() nao funciona 