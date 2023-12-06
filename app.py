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
    with open('data.json', 'w') as f:
        json.dump(data, f)
    return 'OK, JSON recibido'

@app.route('/string', methods=['POST'])
def handle_string():
    global dataSTRING
    dataSTRING = request.data.decode('utf-8')
    print(f'String recibido: {dataSTRING}')
    with open('data.txt', 'w') as f:
        f.write(dataSTRING)
    download_file(data.txt)
    return 'OK, STRING recibido'

from flask import send_file

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return str(e)

