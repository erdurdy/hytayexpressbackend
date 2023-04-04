from fastapi import APIRouter
# from src.auth import auth
import routes  


router = APIRouter()
router.include_router(routes.Offer.router)