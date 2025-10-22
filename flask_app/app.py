from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import *
from database import db as db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os


UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/", endpoint="portada")
def portada():
    avisos = db.get_avisos(5)
    return render_template("portada.html", avisos = avisos) #Recordar cambiar los templates


@app.route("/agregar", methods = ["GET","POST"])
def agregar_aviso():
    if request.method == "POST":
        valido,errores = validar_agregarAviso(request.form, request.files)
        if not valido:
           
           regiones = db.get_regiones()
           comunas = db.get_comunas()

           return render_template("agregar.html", error = errores, regiones = db.get_regiones(), comunas = comunas, formData = request.form)

        fotos = []
        for f in request.files.getlist("foto"):
            filename = secure_filename(f.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            f.save(filepath)
            fotos.append(filename)

        db.crear_aviso(request.form, fotos)
        return redirect(url_for("portada"))
    regiones = db.get_regiones()
    comunas = db.get_comunas()
    return render_template("agregar.html", regiones = regiones, comunas = comunas)



@app.route("/listado")
def listado():
    pagina = int(request.args.get('pagina',1))
    avisos = db.get_avisos_por_pagina(pagina)
    total_Avisos = db.get_total_avisos()
    total_paginas = (total_Avisos+4)//5 

    return render_template( "listado.html", avisos=avisos, pagina_actual=pagina, total_paginas=total_paginas )

    
@app.route("/aviso/<int:aviso_id>")
def detalle_aviso(aviso_id):
    aviso = db.get_aviso_por_id(aviso_id)
    if aviso is None:
        return False, "Aviso no encontrado"
    return render_template("detalle.html", aviso=aviso)


if __name__ == "__main__":
    app.run(debug=True)