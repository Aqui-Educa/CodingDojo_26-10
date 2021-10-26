from flask import Flask, render_template

app = Flask(__name__)


@app.route('/cadastro', methods=['GET'])
def obterCadastro():
    return render_template('cadastro.html')
