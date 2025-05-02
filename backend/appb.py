from flask import Flask, request, jsonify
from math import factorial

app = Flask(__name__)

@app.route('/api/factorial', methods=['POST'])
def calcular_factorial():
    data = request.get_json()
    numero = data.get('numero')
    if numero is None or not isinstance(numero, int) or numero < 0:
        return jsonify({'error': 'Debe enviar un número entero no negativo'}), 400
    resultado = factorial(numero)
    return jsonify({'numero': numero, 'factorial': resultado})

if __name__ == '__main__':
    app.run(port=5001)
