import re 
import filetype
from datetime import datetime



def validar_nombre(nombre: str):
    if not nombre or len(nombre) > 50 or len(nombre) < 3:
        return False
    return bool(re.match(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$", nombre))

def validar_email(email: str):
    if not email or len(email) > 100:
        return False
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email))

def validar_telefono(telefono: str):
    if not telefono:
        return True
    return bool(re.match(r"^\+\d{3}\.\d{8}$", telefono))

def validar_tipo(tipo: str):   
    if not tipo:
        return False
    return tipo.strip().lower() in ['perro', 'gato']

def validar_entero(valor):
    if not valor or not valor.isdigit():
        return False
    valor = int(valor)
    return valor > 0

def validar_unidad_edad(unidad: str):
    return unidad.lower() in ['años', 'meses']

def validar_fecha(fecha: str):
    if not fecha:
        return False
    dt = None
    # 1) intentar datetime-local: YYYY-MM-DDTHH:MM
    try:
        dt = datetime.strptime(fecha, '%Y-%m-%dT%H:%M')
    except ValueError:
        # 2) fallback sólo fecha: YYYY-MM-DD
        try:
            dt = datetime.strptime(fecha, '%Y-%m-%d')
        except ValueError:
            return False
    return dt >= datetime.now()

def validar_texto(texto: str, length: int):
    if not texto:
        return True
    return len(texto) <= length

def validar_sector(sector: str):
    return validar_texto(sector, 100)

def validar_descripcion(descripcion: str):
    return validar_texto(descripcion, 500)


def validar_imagen(archivo):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    if archivo is None:
        return False
    if archivo.filename == "":
        return False
    # check file extension
    ftype_guess = filetype.guess(archivo)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validar_contactar_por(metodo: str, id: str):

    medios_permitidos = ['whatsapp', 'telegram', 'X', 'instagram', 'tiktok', 'otra']

    if not metodo and not id:
        return True
    if not metodo and not id:
        return False
    if metodo.lower() not in medios_permitidos:
        return False
    return 4 <= len(id) <=50


    

def validar_agregarAviso(form, files):
    errores = []
    if not validar_nombre(form.get("nombre")):
        errores.append("Nombre inválido")
    if not validar_email(form.get("email")):
        errores.append("Email inválido")
    if not validar_telefono(form.get("celular", '')):
        errores.append("Celular inválido")
    if not validar_tipo(form.get("tipo")):
        errores.append("Tipo inválido")
    if not validar_entero(form.get("cantidad")):
        errores.append("Cantidad inválida")
    if not validar_entero(form.get("edad")):
        errores.append("Edad inválida")
    if not validar_unidad_edad(form.get("unidad_medida")):
        errores.append("Unidad de edad inválida")
    if not validar_fecha(form.get("fecha_entrega")):
        errores.append("Fecha de entrega inválida")
    if not validar_sector(form.get("sector", '')):
        errores.append("Sector inválido")
    if not validar_descripcion(form.get("descripcion", '')):
        errores.append("Descripción inválida")

    if form.getlist("contactar_por[]"):
        medios = form.getlist("contactar_por[]")
        id_contacto = form.getlist("id-contacto[]")

        for par in zip(medios, id_contacto):
            if not validar_contactar_por(par[0], par[1]):
                errores.append("Método de contacto inválido")

    fotos = files.getlist("foto")
    if not fotos or fotos == [None]:
        errores.append("Se requiere al menos una imagen")
    elif fotos:
        for foto in fotos:
            if not validar_imagen(foto):
                errores.append("Imagen inválida")
    
    return len(errores) == 0, errores

