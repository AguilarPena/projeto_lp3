#importa a class Flask do módulo flask
from flask import Flask
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
    return "<h1>Home Page<h1>"

# /contato - página de contato
@app.route("/contato")
def xxxxx():
    return "<h1>Contato<h1>"

# /produtos - página de produtos
@app.route("/produtos")
def prods():
    return "<h1>Produtos<h1>"

# /servicos - retomar "Nossos serviços"
@app.route("/servicos")
def servs():
    return "<h1>Nossos Serviços<h1>"

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

app.run()