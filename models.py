from sqlmodel import SQLModel, Field, Relationship

class JugadorBase(SQLModel):
    name: str | None = Field(description="Nombre Jugador")
    numero: int | None = Field(description="")
    status: bool | None = Field(description="User status", default=True)

class Jugador(JugadorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

class Estadistica():
    pass


class Partido():
    pass


