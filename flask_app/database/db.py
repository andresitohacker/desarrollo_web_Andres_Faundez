from database.models import *
from sqlalchemy.orm import selectinload
from sqlalchemy import func

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

def avisosPorDia():
    session = SessionLocal()
    data = (session.query(func.date(AvisoAdopcion.fecha_ingreso).label("fecha"),
                         func.count(AvisoAdopcion.id).label("total"),
                         )
                        .group_by("fecha")
                        .order_by("fecha")
                        .all()
                        )
    final = [{"fecha": str(i.fecha), "total": int(i.total)} for i in data]
    session.close()
    return final

def avisosPorTipo():
    session = SessionLocal()
    data = (session.query(AvisoAdopcion.tipo, func.count(AvisoAdopcion.id))
            .group_by(AvisoAdopcion.tipo)
            .all()
    )
    conteo_perro = 0
    conteo_gato = 0
    for tipo, cantidad in data:
        if tipo == "perro":
            conteo_perro = cantidad
        elif tipo =="gato":
            conteo_gato = cantidad
    final = {"perro": conteo_perro, "gato": conteo_gato }
    session.close()
    return final

def avisosPorMes():
    session = SessionLocal()
    data = (session.query(
                func.date_format( AvisoAdopcion.fecha_ingreso, "%Y-%m").label("mes"),
                AvisoAdopcion.tipo,
                func.count(AvisoAdopcion.id).label("total"),
            )
            .group_by("mes",AvisoAdopcion.tipo)
            .order_by("mes")
            .all()
            )
    final = {}
    for mes, tipo, total in data:
        if mes not in final:
            final[mes] = {"mes": mes, "gato": 0, "perro": 0}
        if tipo in ("perro","gato"):
            final[mes][tipo] = int(total)
    session.close()
    return sorted(final.values(), key=lambda x: x["mes"])

def get_comentarios(aviso_id):
    session = SessionLocal()
    data = (session.query(Comentario).filter(Comentario.aviso_id == aviso_id)
            .order_by(Comentario.fecha.desc())
            .all()
            )
    final =[ {"fecha": i.fecha.strftime("%Y-%m-%d %H:%M"), "nombre": i.nombre, "texto": i.texto,} for i in data]
    session.close()
    return final

def crear_Comentario(form, aviso_id):
    session = SessionLocal()
    nuevoComentario = Comentario(
        aviso_id = aviso_id,
        nombre = form.get("nombre"),
        texto = form.get("texto"),
        fecha = datetime.now()
    )
    session.add(nuevoComentario)
    session.commit()
    session.close()
    return nuevoComentario