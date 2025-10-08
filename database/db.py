from models import * 

def get_regiones():
    session = SessionLocal()
    region = session.query(Region).all()
    session.close()
    return region

def get_comunas_by_region(region_id: int):
    session = SessionLocal()
    comunas = session.query(Comuna).filter(Comuna.region_id == region_id).all()
    session.close()
    return comunas

def get_avisos(n, offset=0):
    session = SessionLocal()
    avisos = session.query(AvisoAdopcion).order_by(AvisoAdopcion.fecha_publicacion.desc()).offset(offset).limit(n).all()
    session.close()
    return avisos

def get_avisos_por_pagina(pagina: int):
    offset = (pagina - 1) * 5
    return get_avisos(5, offset)

def get_total_avisos():
    session = SessionLocal
    total = session.query(AvisoAdopcion).count()
    session.close()
    return total

def get_aviso_por_id(aviso_id: int):
    session = SessionLocal()
    aviso = session.query(AvisoAdopcion).filter(AvisoAdopcion.id == aviso_id).first()
    if aviso:
        fotos = aviso.fotos  # Acceder a la relación para cargar las fotos
        contactar = aviso.contactarPor  # Acceder a la relación para cargar los métodos de contacto
    session.close()
    return aviso

def crear_aviso(formulario, fotos):
    session = SessionLocal()
    nuevo_aviso = AvisoAdopcion(
        comuna_id=formulario["comuna"],
        sector=formulario.get("sector",''),
        nombre=formulario["nombre"],
        email=formulario["email"],
        celular=formulario.get("telefono", ''),
        tipo=formulario["tipo"].lower(),
        cantidad=int(formulario["cantidad"]),
        edad=int(formulario["edad"]),
        unidadEdad='a' if formulario["unidadMedidaEdad"] == 'años' else 'm',
        fecha_entrega=formulario["FechaDisponibleEntrega"],
        descripcion=formulario.get("descripcion", '')
    )
    session.add(nuevo_aviso)
    session.flush()

    if formulario.get("contactar_por"):
        tipo_contacto = formulario["contactar_por"].lower()
        if tipo_contacto == 'x':
            tipo_contacto = 'X'     #De esta forma los datos tienen la forma que espera la bd
        contacto = ContactarPor(
            nombre=tipo_contacto,
            identificador=formulario.get("id-contacto", ''),
            actividad_id=nuevo_aviso.id
        )
        session.add(contacto)

    for foto in fotos:
        nueva_foto = Foto(
            ruta_archivo=f"/static/uploads/{foto}",
            nombre_archivo=foto,
            actividad_id=nuevo_aviso.id
        )
        session.add(nueva_foto)

    session.commit()
    session.close()
    return nuevo_aviso
