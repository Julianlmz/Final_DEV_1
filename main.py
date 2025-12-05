from fastapi import FastAPI
#from database import create_tables
import jugador

app = FastAPI(title="Sigmotoa FC")

#create_tables()

app.include_router(jugador.router)

@app.get("/")
async def root():
    return {"message": "sigmotoa FC data"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Bienvenido a sigmotoa FC {name}"}
