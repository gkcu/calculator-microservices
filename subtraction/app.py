from flask import Flask, request, jsonify                           # type: ignore

app = Flask(__name__)

@app.route('/subtract', methods=['GET'])
def subtract():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    return jsonify({"result": a - b})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)