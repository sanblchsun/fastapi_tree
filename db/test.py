from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates("db/templates")

@app.get("/tree")
async def test_tree(request: Request):
    # фиктивные данные
    companies = [
        {
            "name": "Company A",
            "departments": [
                {"name": "Dept 1", "agents": [{"name": "Alice"}, {"name": "Bob"}]},
                {"name": "Dept 2", "agents": []}
            ]
        },
        {
            "name": "Company B",
            "departments": []
        }
    ]
    return templates.TemplateResponse("tree.html", {"request": request, "companies": companies})
