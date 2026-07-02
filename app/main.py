from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router
from contextlib import asynccontextmanager
from app.core.knowledge_service import knowledge

@asynccontextmanager
async def lifespan(app: FastAPI):
    knowledge.load()
    print("Base de conocimiento cargada correctamente.")
    yield

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

app.include_router(router)


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )