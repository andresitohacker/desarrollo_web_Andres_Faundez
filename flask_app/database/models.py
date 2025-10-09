from sqlalchemy import Enum, create_engine, Column, Integer, String, Text, ForeignKey, DateTime, BigInteger
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from datetime import datetime

DB_NAME = "tarea2"
DB_USERNAME = "cc5002" #cc5002
DB_PASSWORD = "programacionweb" #programacionweb
DB_HOST = "localhost"
DB_PORT = 3306


DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future = True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    comunas = relationship("Comuna", back_populates="region")

class Comuna(Base):
    __tablename__ = 'comuna'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)
    region = relationship("Region", back_populates="comunas")
    avisos = relationship("AvisoAdopcion", back_populates="comuna")

class AvisoAdopcion(Base):
    __tablename__ = 'aviso_adopcion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    #Al ahora interesarnos realmente las ultimas publicaciones tenemos que tener claridad de la fecha de publicacion de los avisos

    fecha_ingreso = Column(DateTime, nullable=False, default=datetime.now)
    comuna_id = Column(Integer, ForeignKey('comuna.id'), nullable=False)
    sector = Column(String(100), nullable=True)
    nombre = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    celular = Column(String(12), nullable=False)
    contactarPor = relationship("ContactarPor", back_populates="aviso")
    tipo = Column(Enum('Perro', 'Gato'), nullable=False)
    cantidad = Column(Integer, nullable=False)
    edad = Column(Integer, nullable=False)
    unidad_medida = Column(Enum('Meses', 'Años'), nullable=False)
    fecha_entrega = Column(DateTime, nullable=False)
    descripcion = Column(Text, nullable=True)
    foto = relationship("Foto", back_populates="aviso")
    comuna = relationship("Comuna", back_populates="avisos")

class ContactarPor(Base):
    __tablename__ = 'contactar_por'
    id = Column(Integer, primary_key=True)
    medio = Column(Enum('whatsapp', 'telegram','X','instragram','tiktok','otra'), nullable=True)
    informacion = Column(String(500), nullable=True)
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)
    aviso = relationship("AvisoAdopcion", back_populates="contactarPor")

class Foto(Base):
    __tablename__ = 'foto'
    id = Column(Integer, primary_key=True, autoincrement=True)
    rutaimg = Column(String(255), nullable=False)
    img = Column(String(255), nullable=False)  
    aviso_id = Column(Integer, ForeignKey('aviso_adopcion.id'), nullable=False)
    aviso = relationship("AvisoAdopcion", back_populates="foto")


    