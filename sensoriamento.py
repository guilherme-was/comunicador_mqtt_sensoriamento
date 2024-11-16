import paho.mqtt.client as mqtt
import time
import json
import random
import pandas as pd

# config do Broker MQTT 
THINGSBOARD_HOST = "mqtt.thingsboard.cloud"
ACCESS_TOKENS = [
    "tk-1",  # Sensor 1
    "tk-1",  # Sensor 2
    "tk-1",  # Sensor 3
    "tk-1"   # Sensor 4
]

df = pd.read_csv("devices.csv", delimiter='|')

limites = {
    "temperatura": (0, 50),
    "umidade": (20, 90),
    "ruido": (0, 100), 
    "luminosidade": (0, 1000)
}

# callback verifica conexão
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"Conectado ao ThingsBoard ({userdata['device']})!")
    else:
        print(f"Erro na conexão do {userdata['device']}. Código: {rc}")

# Outliers em faixa aceitavel
def filtrar_outliers(df):
    for coluna, (minimo, maximo) in limites.items():
        df = df[(df[coluna] >= minimo) & (df[coluna] <= maximo)]
    return df

clients = []
for i, token in enumerate(ACCESS_TOKENS):
    client = mqtt.Client(userdata={"device": f"Dispositivo_{i + 1}"})
    client.username_pw_set(token)
    client.on_connect = on_connect
    client.connect(THINGSBOARD_HOST, 1883, 60)
    client.loop_start()
    clients.append(client)

df_filtrado = filtrar_outliers(df)

print("Enviando dados para ThingsBoard...")

try:
    while True:
        for i, client in enumerate(clients):
            if df_filtrado.empty:
                print("Nenhum dado disponível dentro dos limites aceitáveis.")
                continue

            linha = df_filtrado.sample(1).iloc[0]

            dados = {
                "temperatura": linha["temperatura"],
                "umidade": linha["umidade"],
                "ruido": linha["ruido"],
                "luminosidade": linha["luminosidade"]
            }

            dados_enviados = {
                "temperatura": round(float(dados['temperatura']), 2),
                "umidade": round(float(dados['umidade']), 2),
                "ruido": round(float(dados['ruido']), 2),
                "luminosidade": round(float(dados['luminosidade']), 2)
            }

            client.publish("v1/devices/me/telemetry", json.dumps(dados_enviados), qos=1)
            
            print(f"{client._userdata['device']} - Dados enviados: {{'temperatura': {dados_enviados['temperatura']}, 'umidade': {dados_enviados['umidade']}, 'ruido': {dados_enviados['ruido']}, 'luminosidade': {dados_enviados['luminosidade']}}}")

        time.sleep(5)

except KeyboardInterrupt:
    print("Encerrando o envio de dados...")
    for client in clients:
        client.loop_stop()
        client.disconnect()
