import sys, secrets, os
from flask import Flask
from pathlib import Path
import paho.mqtt.client as mqtt

if sys.platform.startswith('win'):
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_urlsafe(16))
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(Path(os.path.abspath(__file__)).parent, 'data.db'))
MQTT_HOST = os.getenv("MQTT_HOST", "broker.hivemq.com")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))



def create_mqtt(on_mess):
    def on_message(client, userdata, message):
        # client.publish(message.topic, message.payload)
        data = str(message.payload.decode('utf-8'))
        print(f"Topic: {message.topic}\nMessage: {data}")
        on_mess(data)
        # print("message qos=",message.qos)
        # print("message retain flag=",message.retain)
    client = mqtt.Client("flask-mqtt")
    client.connect(host=MQTT_HOST, port=MQTT_PORT)
    client.on_message = on_message
    client.loop_start()
   
    return client

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        return app