from flask import Flask, request

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    result = data['first'] + data['second']
    # print(result)
    ans = {"result":result}
    return ans

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['first']-data['second']
    ans = {"result":result}
    return ans

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')