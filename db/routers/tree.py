# db/routers/tree.py
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_session
from db.repositories.tree import get_tree

router = APIRouter()
templates = Jinja2Templates(directory="db/templates")


@router.get("/tree")
async def tree(request: Request, session: AsyncSession = Depends(get_session)):
    companies = await get_tree(session)
    return templates.TemplateResponse(
        "tree.html", {"request": request, "companies": companies}
    )
