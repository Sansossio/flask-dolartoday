from flask import Flask
from services.dolartoday import DolartodayService
import json
app = Flask(__name__)

service = DolartodayService()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dollar')
def dolar_price():
    data = service.getDolarPrice()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/eur')
def eur_price():
    data = service.getEuroPrice()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(
        host="0.0.0.0"
    )
