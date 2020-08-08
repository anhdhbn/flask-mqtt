from flask.globals import session
from config import create_app, create_mqtt
from models import init_app, db
import models
from flask import jsonify, request
import json
app = create_app()
init_app(app)

def save_data(mess):
    data = json.loads(mess)
    entity = models.ExampleData(**data)
    db.session.add(entity)
    db.session.commit()
    print(entity)

mqtt_client = create_mqtt(save_data)
mqtt_client.subscribe("flask-mqtt", 0)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/example/all', methods=['GET'])
def get_all_data():
    all_data = models.ExampleData.query.all()
    return jsonify(models.ExampleData.serialize_list(all_data))

@app.route('/example', methods=['POST'])
def post_data():
    content = request.json
    entity = models.ExampleData(**content)
    db.session.add(entity)
    db.session.commit()
    return jsonify(entity.serialize())