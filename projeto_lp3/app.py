from flask import Flask

app = Flask("Minha App") # nome da minha aplicação/projeto - pode ser qualquer coisa


# página do flask: rota + função

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