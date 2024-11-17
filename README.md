# comunicador_mqtt_sensoriamento

## Configuração do Ambiente MQTT
O MQTT (Message Queuing Telemetry Transport) é um protocolo de comunicação leve e ideal para aplicações IoT. Para gerenciar a comunicação entre os dispositivos de sensoriamento (publicadores) e a aplicação na nuvem (subscritor), você precisará de um broker MQTT, como o Mosquitto.

## Instalação do Broker MQTT (Mosquitto)
No servidor ou na máquina onde o processamento dos dados será feito, execute os seguintes comandos:
```
sudo apt-get update
sudo apt-get install mosquitto mosquitto-clients
sudo systemctl start mosquitto
```

## Instalação da Biblioteca Paho MQTT para Comunicação
Para facilitar a comunicação com o broker MQTT, instale a biblioteca Paho MQTT:
```
pip install paho-mqtt
```
## Execução do Script de Sensoriamento
Após configurar o ambiente, execute o script para iniciar a comunicação de sensoriamento:
```
python3 sensoriamento.py
```

Dashboard para visualização dos dados:
![image](https://github.com/user-attachments/assets/2c804745-36ae-4c16-a4ea-a35274314662)
