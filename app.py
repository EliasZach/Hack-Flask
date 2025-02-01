from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/users", methods=['GET'])
def primerHack():
    return jsonify({'payload':'success'})

@app.route("/user", methods=['POST'])
def segundoHack():
    return jsonify({'payload':'success'})

@app.route("/user", methods=['DELETE'])
def tercerHack():
    return jsonify({'payload':'success'})

@app.route("/user", methods=['PUT'])
def cuartoHack():
    return jsonify({'payload':'success', 'error':False})

@app.route("/api/v1/users", methods=['GET'])
def quintoHack():
    lista = []
    return jsonify({'payload':lista})

@app.route("/api/v1/user", methods=['POST'])
def sextoHack():
    data = request.args
    return jsonify({'payload':data})

@app.route("/api/v1/user/add", methods=['POST'])
def septimoHack():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    data = {'email':email,'name':name,'id':id}
    return jsonify({'payload':data})

@app.route("/api/v1/user/create", methods=['POST'])
def octavoHack():
    data = request.json
    return jsonify({'payload':data})

if __name__ == "__main__":
    app.run(debug=True)