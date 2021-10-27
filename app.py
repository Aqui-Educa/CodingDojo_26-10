from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/', methods=['GET'])
def obterCadastro():
    return render_template('template.html')


@app.route('/cadastrarUsuario', methods=['POST'])
def cadastrarUsuario():

    with open ("cadastro.csv", 'w', encoding="UTF-8", newline="") as cad:
        
        write = csv.writer(cad, delimiter=',')
        usuario = request.json
        user = [usuario["id"], usuario["nome"], usuario["cpf"], usuario["telefone"], usuario["email"], usuario["vaga"], usuario["endereco"]]
        write. writerow(user)
    
    return "Cadastro realizado com sucesso!"