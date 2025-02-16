from flask import Flask, request, jsonify                           # type: ignore

app = Flask(__name__)

@app.route('/divide', methods=['GET'])
def divide():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    if b == 0:
        return jsonify({"error": "Division by zero"}), 400
    return jsonify({"result": a / b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)