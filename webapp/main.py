from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from .tasks import check_compliance
from pathlib import Path

app = FastAPI()
BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/check")
async def check_compliance_endpoint(compliance_url: str = Form(...), product_url: str = Form(...)):
    task = check_compliance.delay(compliance_url, product_url)
    return {"task_id": task.id}
