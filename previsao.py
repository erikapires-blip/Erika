import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# 1. Buscar os dados da API do Open-Meteo para Goiânia (Latitude: -16.68, Longitude: -49.25)
url = "https://api.open-meteo.com/v1/forecast?latitude=-16.68&longitude=-49.25&hourly=temperature_2m&timezone=America/Sao_Paulo"
resposta = requests.get(url)
dados = resposta.json()

# 2. Organizar os dados usando o Pandas
horas = dados["hourly"]["time"]
temperaturas = dados["hourly"]["temperature_2m"]

# Criar uma tabela (DataFrame) com os dados
df = pd.DataFrame({"Hora": horas, "Temperatura": temperaturas})

# Converter o texto da hora para um formato que o Python entenda como tempo
df["Hora"] = pd.to_datetime(df["Hora"])

# Pegar apenas as próximas 24 horas para o gráfico não ficar gigante
df = df.head(24)

# 3. Criar o gráfico com o Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(df["Hora"], df["Temperatura"], marker='o', color='orange', linewidth=2)

# Customizar o gráfico
plt.title(f"Previsão do Tempo para Goiânia - Atualizado em {datetime.now().strftime('%d/%m/%Y')}", fontsize=14, fontweight='bold')
plt.xlabel("Horário", fontsize=12)
plt.ylabel("Temperatura (°C)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)

# Rotacionar as horas no eixo X para caberem melhor
plt.xticks(rotation=45)
plt.tight_layout()

# 4. Salvar o gráfico como imagem
plt.savefig("previsao_goiania.png")
print("Gráfico gerado com sucesso!")
