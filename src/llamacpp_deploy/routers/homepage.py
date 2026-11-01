from fastapi import APIRouter

from llamacpp_deploy import config

router = APIRouter(tags=["homepage"])


@router.get("/")
def home():
    return {
        "llama.cpp model": config.MODELNAME or "unknown",
        "version": config.VERSION,
        "hostname": config.HOSTNAME,
    }
