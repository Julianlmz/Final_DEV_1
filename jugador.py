from fastapi import APIRouter, HTTPException, Query
from database import SessionDep
from models import Jugador, JugadorCreate, JugadorUpdate, JugadorBase, Estados
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

@router.get("/", response_model=List[Jugador])
def read_jugadores(estado: Estados = Query(default=None), session: SessionDep = None):
    query = select(Jugador)
    if estado:
        query = query.where(Jugador.estado == estado)
    empleados = session.exec(query).all()
    return empleados

@router.get("/{juagdor_id}", response_model=Jugador)
def read_jugador(session: SessionDep, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Jugador no encontrado")
    return jugador

@router.patch("/{jugador_id}", response_model=Jugador)
def update_jugador(jugador_id: int, jugador_update: JugadorCreate, session: SessionDep):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    jugador.nombre = jugador_update.nombre
    jugador.numero = jugador_update.numero
    jugador.fecha_nacimiento = jugador_update.fecha_nacimiento
    jugador.nacionalidad = jugador_update.nacionalidad
    jugador.altura = jugador_update.altura
    jugador.peso = jugador_update.peso
    session.commit()
    session.refresh(jugador)
    return jugador

@router.delete("/jugador_id}")
def delete_jugador(session: SessionDep, jugador_id: int):
    jugador = session.get(Jugador, jugador_id)
    if not jugador:
        raise HTTPException(status_code=404, detail="jugador no encontrado")

    session.delete(jugador)
    session.commit()
    return {"ok": True, "detail": "jugador eliminado"}