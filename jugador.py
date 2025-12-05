from fastapi import APIRouter, HTTPException
from database import SessionDep
from models import Jugador, JugadorCreate, JugadorRead, JugadorUpate, JugadorBase
from typing import List
from sqlmodel import select

router = APIRouter(tags=["Jugador"], prefix="/jugador")

@router.post("/", response_model=Jugador, status_code=201)
async def create_jugador(new_jugador: JugadorCreate, session: SessionDep):
    jugador = Jugador.model_validate(new_jugador)
    session.add(jugador)
    await session.commit()
    await session.refresh(jugador)
    return jugador

@router.get("/", response_model=List[JugadorRead])
def read_jugadores(session: SessionDep):
    jugadores = session.exec(select(Jugador)).all()
    return jugadores

@router.get("/{juagdor_id}", response_model=JugadorRead)
def read_jugador(session: SessionDep, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

@router.patch("/{jugador_id}", response_model=JugadorRead)
def update_jugador(session: SessionDep, jugador_id: int, jugador_update: JugadorBase):
    db_jugador = session.get(Jugador, jugador_id)
    if not db_jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")

    jugador_data = jugador_update.model_dump(exclude_unset=True)
    db_jugador.sqlmodel_update(jugador_data)

    session.add(db_jugador)
    session.commit()
    session.refresh(db_jugador)
    return db_jugador

@router.delete("/jugador_id}")
def delete_jugador(session: SessionDep, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="jugador no encontrado")

    session.delete(jugador)
    session.commit()
    return {"ok": True, "detail": "jugador eliminado"}