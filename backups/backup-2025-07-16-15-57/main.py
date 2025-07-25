from fastapi import FastAPI, Request from fastapi.responses 
import HTMLResponse from fastapi.staticfiles import 
StaticFiles from fastapi.templating import Jinja2Templates 
app = FastAPI()
# mount static files if needed (optional)
app.mount("/static", StaticFiles(directory="static"), 
name="static")
# templates path
templates = Jinja2Templates(directory="templates") 
@app.get("/", response_class=HTMLResponse) async def 
read_index(request: Request):
    return templates.TemplateResponse("index.html", 
    {"request": request})
@app.get("/ping") def ping():
    return {"message": "KasbAI running successfully"}
