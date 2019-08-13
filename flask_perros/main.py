from flask import Flask
from flask import render_template

import forms
app = Flask(__name__)
@app.route('/')
def index():
    #Instanciando de la clase GeneracionForm y const obj  genform
    genform=forms.GeneracionForm()
    title="Adopta tu perro"
    return render_template("index.html",title=title,form=genform)
if __name__ == '__main__':
    app.run(debug=True,port=8080)    