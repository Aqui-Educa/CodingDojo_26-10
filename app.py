from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/', methods=['GET'])
def obterCadastro():
    return render_template('template.html')


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():

    usuario = request.json
    with open("cadastro.csv", 'a', encoding="UTF-8", newline="") as cad:

        write = csv.writer(cad, delimiter=';')

        print(usuario)
        user = [usuario['id'], usuario['nome'], usuario['cpf'], usuario['telefone'],
                usuario['email'], usuario['vaga'], usuario['endereco']]
        print(usuario)
        print(user)

        write.writerow(user)

    return "Cadastro realizado com sucesso!"
