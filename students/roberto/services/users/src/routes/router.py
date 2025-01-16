from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/.health")
def health():
  return {"status": "ok"}
