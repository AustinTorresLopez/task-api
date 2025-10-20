from pydantic import BaseModel

class TaskIn(BaseModel): #POST (Crear una nueva tarea)
    title: str

class TaskUpdate(BaseModel): #PUT (Actualizar)
    title: str | None = None
    done: bool | None = None

class TaskOut(BaseModel): #Devolver datos al cliente (la respuesta de la API)
    id: int
    title: str
    done: bool

    class Config:
        orm_mode = True

