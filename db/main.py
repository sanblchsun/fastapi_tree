# db/main.py
from fastapi import FastAPI
from db.routers.tree import router as tree_router

app = FastAPI(title="Company Tree App")

app.include_router(tree_router)
