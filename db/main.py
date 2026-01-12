from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db.routers.tree import router as tree_router

app = FastAPI(title="Company Tree")

app.include_router(tree_router)

# # опционально
# app.mount("/static", StaticFiles(directory="static"), name="static")
