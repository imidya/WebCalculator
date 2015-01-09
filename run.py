# import web
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])
def ezCalculator():
    if request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
