from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("База стала кринжем")
    await create_tables()
    print("База готова стать базой")
    yield
    print("оффнуто нахуй")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)



