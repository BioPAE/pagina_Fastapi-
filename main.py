from datetime import datetime

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse(
        request=request, name="index.html",
    )


@app.get("/etapas", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse(
        request=request, name="etapas.html", 
    )


@app.get("/linaje", response_class=HTMLResponse)
async def contacto(request: Request):
    return templates.TemplateResponse(
        request=request, name="linaje.html", 
    )
    
@app.get("/secretos", response_class=HTMLResponse)
async def secretos(request: Request):
    return templates.TemplateResponse(
        request=request, name="secretos.html", 
    )