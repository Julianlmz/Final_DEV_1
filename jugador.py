from fastapi import APIRouter, HTTPException
from database import SessionDep
from models import Jugador, Estados, PieDominante, Posicion, JugadorCreate
from typing import List

router = APIRouter(tags=["Jugador"], prefix="/jugador")

@router.post("/", response_model=Jugador, status_code=201)
async def create_jugador(new_jugador: JugadorCreate, session: SessionDep):
    jugador = Jugador.model_validate(new_jugador)
    session.add(jugador)
    session.commit()
    session.refresh(jugador)
    return jugador
