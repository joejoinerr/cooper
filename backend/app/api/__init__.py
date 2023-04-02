from fastapi import APIRouter

from app.api.endpoints import coupons


api_router = APIRouter()
api_router.include_router(coupons.router, prefix='/coupons', tags=['coupons'])
