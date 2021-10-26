from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def obterCadastro():
    return render_template('template.html')


