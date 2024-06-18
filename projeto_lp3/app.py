#importa a class Flask do módulo flask
from flask import Flask, render_template
from validate_docbr import CPF, CNPJ

#instancia um objeto flask que representa a aplicação
app = Flask("Minha App") # nome da minha aplicação/projeto - pode ser qualquer coisa

cpf = CPF()
cnpj = CNPJ()

# página do flask: rota + função
#função: pyhton com retorno (string, template, outro)

# /home page - página inicial
@app.route("/")
def home():
    return render_template("home.html")

# /contato - página de contato
@app.route("/contato")
def xxxxx():
    return render_template("contato.html")

# /produtos - página de produtos
@app.route("/produtos")
def produtos():
    lista_produtos = [
        {"nome": "Coca-Cola", "descricao": "Mata a sede"},
        {"nome": "Doritos", "descricao": "Suja a mão"},
        {"nome": "Chocolate", "descricao": "Bom"}
    ]
    return render_template("produtos.html", produtos=lista_produtos)

# /servicos - retomar "Nossos serviços"
@app.route("/servicos")
def servs():
    return "<h1>Nossos Serviços<h1>"

'''''
# /gerar-cpf - retomar CPF aleatório
@app.route("/gerar-cpf")
def cpf():
    return cpf.generate(True)
    #return f"CPF: {cpf.generate(True)}"

# /gerar-cnpj - retomar CNPJ aleatório
@app.route("/gerar-cnpj")
def cnpj():
    return cnpj.generate(True)
    #return f"<h1>CNPJ: {cnpj.generate(True)}<h1>"

'''''

@app.route("/gerar-cpf")
def gcpf():
    return cpf.generate(True)
# /produtos - página de produtos
@app.route("/gerar-cnpj")
def gcnpj():
    return cnpj.generate(True)

app.run()

