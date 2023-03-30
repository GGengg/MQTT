import paho.mqtt.client

broker_address = "broker.hivemq.com"
broker_port = 1883
topic = "FTM-RTT"


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)


def on_disconnect(client, userdata, rc):
    print(f"Disconnected with result code {rc}")


def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode('utf-8')}")


client = paho.mqtt.client.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect(broker_address, broker_port)
client.loop_forever()