from wtforms import Form
from wtforms import StringField

class GeneracionForm(Form):
    username= StringField("Usuario")
    email =StringField("Correo")
    comment =StringField("Comentario")
    nuevocampo =StringField("Ejemplo")
