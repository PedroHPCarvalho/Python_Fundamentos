from datetime import date, datetime, time, timedelta

tipo_carro = "M" # P M G
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == "P":
  data_estimada = data_atual - timedelta(minutes=tempo_pequeno)
  print(f"O carro chegou: {data_atual} e ficara pronto {data_estimada}")
if tipo_carro == "M":
  data_estimada = data_atual - timedelta(minutes=tempo_medio)
  print(f"O carro chegou: {data_atual} e ficara pronto {data_estimada}")
if tipo_carro == "G":
  data_estimada = data_atual - timedelta(minutes=tempo_grande)
  print(f"O carro chegou: {data_atual} e ficara pronto {data_estimada}")

print(date.today() - timedelta(days=1))

resultado = datetime(2021,4,12,21,51) - timedelta(hours=1)
print(resultado.time())
print(resultado.date())
