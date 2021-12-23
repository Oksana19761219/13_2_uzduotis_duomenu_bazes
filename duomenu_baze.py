from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime


engine = create_engine('sqlite:///darbuotojai.db')
Base = declarative_base()

class Darbuotojai(Base):
    __tablename__ = 'darbuotoju_duomenys'
    id = Column(Integer, primary_key=True)
    vardas = Column("vardas", String)
    pavarde = Column("pavarde", String)
    gimimo_data = Column("gimimo_data", DateTime)
    pareigos = Column("pareigos", String)
    atlyginimas = Column("atlyginimas", Float)
    dirba_nuo = Column("nuo_kada_dirba", DateTime)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas, dirba_nuo=datetime.datetime.now()):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas
        self.dirba_nuo = dirba_nuo

    def __repr__(self):
        return f"""
        vardas: {self.vardas}
        pavardė: {self.pavarde}
        gimimo data: {self.gimimo_data}
        pareigos: {self.pareigos}
        atlyginimas: {self.atlyginimas}
        dirba nuo: {self.dirba_nuo}
        """
Base.metadata.create_all(engine)