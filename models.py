from sqlmodel import SQLModel, Field, Relationship
from enum import Enum
from typing import List

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

class JugadorEstadistica(SQLModel, table=True):
    jugador_id: int = Field(foreign_key="jugador.id", primary_key=True)
    estadistica_id: int = Field(foreign_key="estadistica.id", primary_key=True)

class JugadorBase(SQLModel):
    name: str | None = Field(description="Nombre Jugador")
    numero: int | None = Field(description="Numero de Camiseta")
    nacionalidad: str | None = Field(description="Nacionalidad del Jugador")
    estatura: int | None = Field(description="Estatura del Jugador")
    peso: int | None = Field(description="Peso del Jugador en Kg")
    pie_dominante: PieDominante
    estado: Estados

class Jugador(JugadorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    estaditicas: List["Estadistica"] = Relationship(back_populates="jugadores", link_model=JugadorEstadistica)

class JugadorCreate(JugadorBase):
    pass

class Estadistica():
    pass


class Partido():
    pass


