import json
from flask import Flask, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'mongodb',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

class Car(db.Document):
    idCar = db.SequenceField()
    cor = db.StringField()
    placa = db.StringField()
    ano = db.IntField()
    modelo = db.StringField()

  
    def to_json(self):
        return {
            "idCar": self.idCar,
            "cor": self.cor,
            "placa": self.placa,
            "ano": self.ano,
            "modelo": self.modelo
        }


@app.route('/cars', methods=['GET'])
def query_records():
    record = json.loads(request.data)

    try:
        car = Car.objects.get(cor=record['cor'], placa=record['placa'], ano=str(record['ano']), modelo=record['modelo'])
        output = {'idCar': int(car.idCar)}
        print(output)
        return output, 200
    except:
        return "Not found", 404

@app.route('/cars', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    try:
        car = Car.objects.get(cor=record['cor'], placa=record['placa'], ano=str(record['ano']), modelo=record['modelo'])
        return "Object Already Exists", 409
    except:
        car = Car(cor=record['cor'], placa=record['placa'], ano=record['ano'], modelo=record['modelo'])
        car.save()
        return jsonify(car.to_json())

@app.route('/cars', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    try:
        car = Car.objects.get(cor=record['cor'], placa=record['placa'], ano=str(record['ano']), modelo=record['modelo'])
        car.delete()
        return jsonify(car.to_json()), 200 
    except:
        return "Object not found", 404

@app.route('/cars', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    try:
        car = Car.objects.get(placa=record['placa'])
        car.update(cor=record['cor'], ano=str(record['ano']), modelo=record['modelo'])
        return jsonify(record), 200
    except:
        return "Not found", 404



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
