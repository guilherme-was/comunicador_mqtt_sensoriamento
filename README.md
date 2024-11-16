# comunicador_mqtt_sensoriamento

## 1. Configuração do Ambiente MQTT
O MQTT é um protocolo de comunicação leve ideal para IoT. Você precisará de um broker MQTT (como o Mosquitto) para gerenciar a comunicação entre os dispositivos de sensoriamento (publicadores) e a aplicação na nuvem (subscritor).

Instalação do Broker MQTT (Mosquitto): No servidor ou na máquina onde o processamento dos dados será feito:
```
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients
sudo systemctl start mosquitto
```

Paho Mqtt para comunicacao MQTT
```
pip install paho-mqtt
```
Execução:

python3 sensoriamento.py
