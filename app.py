from flask import Flask, request, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://127.0.0.1:5500", "http://hain.umag.cl/~arilopez/"]}})
global dataJSON
global dataSTRING
@app.route('/json', methods=['POST'])

def handle_json():
    global dataJSON
    data = json.loads(request.data.decode('utf-8'))
    dataJSON = data['object']['name']
    print(f'Data recibida: {dataJSON}')
    # Aquí puedes guardar 'data' en la variable que quieras
    return 'OK, JSON recibido'

@app.route('/string', methods=['POST'])
def handle_string():
    global dataSTRING
    dataSTRING = request.data.decode('utf-8')
    print(f'String recibido: {dataSTRING}')
    # Aquí puedes guardar 'data' en la variable que quieras
    return 'OK, STRING recibido'
