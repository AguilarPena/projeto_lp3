#importa a class Flask do módulo flask
from flask import Flask, render_template, request
from validate_docbr import CPF, CNPJ

lista_produtos = [
        {"nome": "Coca-Cola", "descricao": "Mata a sede", "imagem": "https://www.piramidesdistribuidora.com.br/images/products/3709-coca-cola-zero-lata-350ml-12un.20240613133557.png"},
        {"nome": "Doritos", "descricao": "Suja a mão", "imagem": "https://images-americanas.b2w.io/produtos/01/00/img/2638457/4/2638457405_1GG.jpg"},
        {"nome": "Chocolate", "descricao": "É bom", "imagem": "https://img.sitemercado.com.br/produtos/4dbe50451cec9ef0765045abfd6342082b399c04f0ee7ec680080f573e2e5b6c_full.jpg"}
    ]

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

@app.route("/cpf")
def gcpf():
    vcpf = cpf.generate(True)
    return render_template("cpf.html", cpf = vcpf)


@app.route("/cnpj")
def gcnpj():
    vcnpj = cnpj.generate(True)
    return render_template("cnpj.html", cnpj = vcnpj)

@app.route("/termos")
def termos():
    return render_template("termos.html")

@app.route("/politica")
def politica():
    return render_template("politica.html")

@app.route("/uso")
def uso():
    return render_template("uso.html")

#GET /produtos/cadastro (rota que devolve o form)
@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro_produto.html")

#POST /produtos (produtos que vai lidar com os dados envidos pelo form)
#enviados pelo form
#acessar o objeto request (importar)

@app.route("/produtos", methods=['POST'])
def salvar_produto():
    
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    
    produto = {"nome": nome, "descricao": descricao, "imagem": ""}
    lista_produtos.append(produto)

    return render_template("produtos.html", produtos=lista_produtos)

app.run()

