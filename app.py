from flask import Flask, request, render_template, redirect, url_for, session
from utils.validations import none
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os


UPLOAD_FOLDER = 'static/uploads'

app = Flask(__name__)

app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def portada():
    avisos = db.get_avisos(5)
    return render_template("portada.html", avisos = avisos) #Recordar cambiar los templates


@app.route("/agregar", methods = ["GET","POST"])
def agregar_aviso():
    if request.method == "POST":
        error = ""
        if validar_agregarAviso():

            db.crear_aviso(request.form, request.files)
            return redirect(url_for("portada"))
            
        else:
            error += "Uno de los campos es invalido"

        if error:
            return render_template("agregar.html", error = error)
    elif request.method == "GET":
        regiones = db.get_regiones()
        return render_template("agregar.html", regiones=regiones)

@app.route("/listado")
def listado():
    pagina = int(request.args.get('pagina',1))
    avisos = db.get_avisos_por_pagina(pagina)
    total_Avisos = db.get_total_avisos()
    total_paginas = (total_Avisos+5)//5 

    