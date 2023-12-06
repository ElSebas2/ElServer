from flask import Flask, request, json
from flask_cors import CORS
import os

dir_path = os.getcwd()
for filename in os.listdir(dir_path):
    print(filename)
    
app = Flask(__name__)
CORS(app)
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
    for filename in os.listdir(dir_path):
        print(filename)
    return 'OK, JSON recibido'

@app.route('/string', methods=['POST'])
def handle_string():
    global dataSTRING
    dataSTRING = request.data.decode('utf-8')
    print(f'String recibido: {dataSTRING}')
    with open('data.txt', 'w') as f:
        f.write(dataSTRING)
    for filename in os.listdir(dir_path):
        print(filename)
            
    return 'OK, STRING recibido'

from flask import send_file

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        response = send_file(filename, as_attachment=True)
        os.remove(filename)
        return response
    except Exception as e:
        return str(e)

