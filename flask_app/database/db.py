from database.models import *
from sqlalchemy.orm import selectinload

def get_regiones():
    session = SessionLocal()
    region = session.query(Region).all()
    session.close()
    return region

def get_comunas():
    session = SessionLocal()
    comunas = session.query(Comuna).all()
    session.close()
    return comunas

def get_avisos(n, offset=0):
    session = SessionLocal()
    
    avisos = session.query(AvisoAdopcion)\
        .options(
            selectinload(AvisoAdopcion.comuna), 
            selectinload(AvisoAdopcion.fotos)           #Si no cargo las relaciones de esta forma me da error
        )\
        .order_by(AvisoAdopcion.fecha_ingreso.desc())\
        .offset(offset)\
        .limit(n)\
        .all()
        
    session.close()
    return avisos

def get_avisos_por_pagina(pagina: int):
    offset = (pagina - 1) * 5
    return get_avisos(5, offset)

def get_total_avisos():
    session = SessionLocal()
    total = session.query(AvisoAdopcion).count()
    session.close()
    return total

def get_aviso_por_id(aviso_id: int):
    session = SessionLocal()
    aviso = session.query(AvisoAdopcion).options(
        selectinload(AvisoAdopcion.fotos),
        selectinload(AvisoAdopcion.contactarPor),
        selectinload(AvisoAdopcion.comuna)
    ).filter(AvisoAdopcion.id == aviso_id).first()
    session.close()
    return aviso

def crear_aviso(formulario, fotos):
    session = SessionLocal()
    nuevo_aviso = AvisoAdopcion(
        comuna_id=formulario["comuna"],
        sector=formulario.get("sector",''),
        nombre=formulario["nombre"],
        email=formulario["email"],
        celular=formulario.get("celular", ''),
        tipo=formulario["tipo"].lower(),
        cantidad=int(formulario["cantidad"]),
        edad=int(formulario["edad"]),
        unidad_medida='a' if formulario["unidad_medida"] == 'años' else 'm',
        fecha_entrega=formulario["fecha_entrega"],
        descripcion=formulario.get("descripcion", '')
    )
    session.add(nuevo_aviso)
    session.flush()

    medios = formulario.getlist("contactar_por[]")
    id_contacto = formulario.getlist("id-contacto[]")
    for medio, id in zip(medios, id_contacto):
        if not medio:
            continue
        if medio.lower() == 'x':
            medio = 'X'
        nuevo_medio = ContactarPor(
            nombre=medio,
            identificador=id,
            actividad_id=nuevo_aviso.id
        )
        session.add(nuevo_medio)

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
