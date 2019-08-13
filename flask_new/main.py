#Importando la libreria de Flask
from flask import Flask
from flask import request
from flask import render_template
#Asignar a una aplicacion
app = Flask(__name__,template_folder="templates_codigo")
#Decorador
@app.route('/')
def login():
    return "Esta es mi pagina perritos en codiGO-Tecsup"

@app.route("/perritos")
def perritos():
    return "Este es la seccion de perritos"  

@app.route("/clientes")
def clientes():
    param = request.args.get("usuario","parametro usuario vacio")
    param2 = request.args.get("clave","parametro clave vacio")
    return "El Cliente es :{},{}".format(param,param2)       

@app.route("/usuario")
@app.route("/usuario/<codigo>")
@app.route("/usuario/<codigo>/<int:valor>")
def usuarios(codigo="Valor o por defecto",valor=0):
    return "Los datos del usuario son:{} {}".format(codigo,valor)

@app.route("/front")
def index():
    return render_template("index.html")

@app.route("/frontags/<curso>")
def cursos(curso="Flask"):
    edadmascota = 12
    mascotas = ['BOBY','PLUTO','CHOCOLATE']
    return render_template("mascotas.html",noentiendo=curso,edad=edadmascota,lista=mascotas)
    
@app.route("/main")
def main():
    return render_template("main.hmtl")

if __name__ == '__main__':
    app.run( debug = True, port=8000)