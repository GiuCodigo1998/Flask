from flask import Flask,render_template,abort
app =Flask(__name__)

@app.route('/tecsup')
@app.route('/tecsup/<profesion>')
def mensaje(profesion=None):
    return render_template("template1.html",prof=profesion)

@app.route('/calculodolar/<valor>/<cantidad>')
def montosoles(valor,cantidad):
    try:
        monto=float(valor)*float(cantidad) 
    except:
        abort(404)
    return render_template("template2.html",val=valor,can=cantidad,
            res=monto)           
@app.route('/paginas')
def paginas():
    webs =[ {"url":"http://www.google.com","texto":"Google"},
            {"url":"https://codigo.edu.pe","texto":"Codigo"},
            {"url":"https://palletsprojects.com/p/flask/","texto":"Flask"}
    ]
    #webs =[]
    return render_template("template4.html",sitios=webs)

@app.route('/mascotas')
def pagmascotas():
    webs =[ {"url":"https://www.segurossura.com.uy/wp-content/uploads/2018/12/mascotas-sura.jpg","nombre":"Boby"},
            {"url":"https://estaticos.muyinteresante.es/media/cache/760x570_thumb/uploads/images/article/5c3871215bafe83b078adbe3/perro.jpg","nombre":"Pluto"},
            {"url":"https://ichef.bbci.co.uk/news/410/cpsprodpb/15665/production/_107435678_perro1.jpg","nombre":"Charlie"}
    ]
    #webs =[]
    return render_template("template4.html",sitios=webs)

@app.route('/tabla/<valor>')
def generarmultiplo(valor):
    try:
        numero = int(valor)
    except:
        abort(404)
    return render_template("template3.html",num=numero)                    

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template("error.html",error="Pagina No encontrada"),404

if __name__ == '__main__':
    app.run(debug=True,port=8000)