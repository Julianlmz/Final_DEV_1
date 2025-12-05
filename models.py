from sqlmodel import SQLModel, Field, Relationship
from enum import Enum

class Estado(str,Enum):
    Activo = "Activo"
    Inactivo = "Inactivo"

class PieDominante(str,Enum):
    Zurdo = "Zurdo"
    Diestro = "Diestro"

class Posicion(str,Enum):
    DefensaLateral = "Defensa Lateral"
    DefensaCentral = "Defensa Central"
    VolanteDefensivo = "Volante Defensivo"
    Extremo = "Extremo"
    Delantero = "Delantero"

class JugadorBase(SQLModel):
    name: str | None = Field(description="Nombre Jugador")
    numero: int | None = Field(description="Numero de Camiseta")
    nacionalidad: str | None = Field(description="Nacionalidad del Jugador")
    estatura: int | None = Field(description="Estatura del Jugador")
    peso: int | None = Field(description="Peso del Jugador en Kg")
    pie_dominante: PieDominante
    estado: Estado

class Jugador(JugadorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class Estadistica():
    pass


class Partido():
    pass


