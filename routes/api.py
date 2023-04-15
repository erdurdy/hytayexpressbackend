from fastapi import APIRouter
# from src.auth import auth
import routes  


router = APIRouter(
    prefix="/api/v1"
)
router.include_router(routes.Offer.router)
router.include_router(routes.Action.router)
router.include_router(routes.ActionType.router)
router.include_router(routes.Container.router)