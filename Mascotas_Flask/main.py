from flask import Flask,render_template,abort

app =Flask(__name__)


@app.route('/')
def main_perrito():
   return render_template("index.html")

@app.errorhandler(404)
def pagina_no_encontrada(error):
   return render_template("error.html",error="Pagina No encontrada"),404



if __name__ == '__main__':
   app.run(debug=True,port=8000)