from fastapi import FastAPI

from llamacpp_deploy.routers import homepage

app = FastAPI()

app.include_router(homepage.router)
