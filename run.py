# import web
from flask import Flask, render_template, request, jsonify
from calculator import Calculator

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def ezCalculator():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/cal', methods=['POST'])
def cal():
    if request.method == 'POST':
        formula = request.form.get('formula')
        if formula is not None:
            c = Calculator()
            result = c.cal(formula)
            return jsonify({'result': result, 'msg': 'ok'})
        else:
            return jsonify({'msg': 'formula is none.'})
    return jsonify({'msg': 'error'})


if __name__ == '__main__':
    app.run()
