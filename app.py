from flask import Flask, render_template, request
import csv, json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def obterCadastro():
    return render_template('template.html')


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():
    # antes era request.json 
    usuario = request.data
    # usuario retorna uma string, abaixo converte em json
    usuario = json.loads(usuario)
    with open("cadastro.csv", 'a', newline="") as cad:
        write = csv.writer(cad, delimiter=',')
        user = [usuario['id'], usuario['nome'], usuario['cpf'], usuario['telefone'], usuario['email'], usuario['vaga'], usuario['endereco']]
        write.writerow(user)

    return {'message': 'Salvo com sucesso (CONSOLE)'}
