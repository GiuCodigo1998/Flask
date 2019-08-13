#Importando la liberia de Flask
from flask import Flask
from flask import request
from flask import render_template
#Asignar a una aplicacion
app = Flask(__name__)
#Decorador 
@app.route('/')
def login():
    return "Esta es mi pagina de perritos de GIU"

@app.route("/perritos")
def perritos():
    return "Este es la seccion de perritos"

@app.route("/clientes")
def cleintes():
    param = request.args.get("usuario","parametro usuario vacio")
    param2 = request.args.get("clave","parametro clave vacio")
    return "El cliente es: {}, {}".format(param,param2)

@app.route("/usuario")
@app.route("/usuario/<codigo>")
@app.route("/usuario/<codigo>/<int:valor>")
def usuario(codigo="Valor 0 por defecto", valor=0):
    return "Los datos del usuario son: {}, {}".format(codigo,valor)

@app.route("/primer")
def index():
    return render_template("index.html")

@app.route("/front")
@app.route("/front/<tag>")
def cursos(tag="Flask"):
    return render_template("cursos.html", envia=tag)

if __name__ == '__main__':
    app.run(debug = True, port=8000)