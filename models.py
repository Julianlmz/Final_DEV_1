from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from typing import List, Optional
from datetime import date

class Estados(str, Enum):
    ACTIVO = "ACTIVO"
    INACTIVO = "INACTIVO"
    LESIONADO= "LESIONADO"
    AMONESTADO= "AMONESTADO"

class PieDominante(str,Enum):
    Zurdo = "Zurdo"
    Diestro = "Diestro"

class Posicion(str,Enum):
    ARQUERO = "ARQUERO"
    DEFENSA_C= "DEFENSA CENTRAL"
    DEFENSA_L = "DEFENSA LATERAL"
    VOLANTE_D = "VOLANTE DEFENSIVO"
    VOLANTE_O = "VOLANTE OFENSIVO"
    VOLANTE_C = "VOLANTE CENTRAL"
    VOLANTE_E = "VOLANTE EXTREMO"
    DELANTERO_C = "DELANTERO CENTRAL"
    DELANTERO_P = "DELANTERO PUNTA"

class PartidoBase(SQLModel): 
    fecha: date 
    rival: str 
    goles: int 
    golesrival: int 
    resultado: str 
    estadisticas: List["Estadistica"] = Relationship(back_populates="partido")

class Partido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 

def determinar_resultado(self):
    if self.goles > self.golesrival:
        self.resultado = "Victoria"
    elif self.goles < self.golesrival:
        self.resultado = "Derrota"
    else:
        self.resultado = "Empate"

class EstadisticaBase(SQLModel): 
    jugador_id: int = Field(foreign_key="jugador.id") 
    partido_id: int = Field(foreign_key="partido.id") 
    minutos_jugados: int 
    goles: int 
    tarjetas: int 
    jugador: "Jugador" = Relationship(back_populates="estadisticas") 
    partido: "Partido" = Relationship(back_populates="estadisticas")

class Estadistica(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 

class JugadorBase(SQLModel): 
    nombre: str 
    numero: int = Field(ge=1, le=99, unique=True) 
    fecha_nacimiento: date 
    nacionalidad: str 
    altura: float 
    peso: float 
    pie_dominante: PieDominante
    posicion: Posicion
    estado: Estados = Field(default=Estados.ACTIVO) 
    estadisticas: List[EstadisticaBase] = Relationship(back_populates="jugador")

class Jugador(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True) 

class JugadorCreate(JugadorBase):
    pass

class JugadorUpdate(JugadorBase):
    pass

