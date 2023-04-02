import json

from fastapi import APIRouter, HTTPException

from app.db import coupon_db
from app.schemas.coupon import (
    CouponBase,
    Coupon,
    CouponCreate,
    CouponUpdate,
    CouponList
)


router = APIRouter()


def coupon_to_dict(coupon: CouponBase):
    return json.loads(coupon.json())


@router.get('', response_model=CouponList)
def list_coupons():
    res = coupon_db.fetch()
    all_coupons = res.items
    while res.last:
        res = coupon_db.fetch(last=res.last)
        all_coupons += res.items
    return CouponList(coupons=[Coupon(**c) for c in all_coupons])


@router.post('', status_code=201, response_model=Coupon)
def create_coupon(coupon: CouponCreate):
    return coupon_db.insert(coupon_to_dict(coupon))


@router.get('/{coupon_key}', response_model=Coupon)
def get_coupon_by_id(coupon_key: str):
    try:
        return coupon_db.fetch({'key': coupon_key}, limit=1).items[0]
    except IndexError as e:
        raise HTTPException(status_code=404, detail='Coupon not found.') from e


@router.put('/{coupon_key}', response_model=Coupon)
def update_coupon(coupon_key: str, coupon: CouponUpdate):
    coupon_db.update(coupon_to_dict(coupon), key=coupon_key)
    return coupon_db.fetch({'key': coupon_key}, limit=1).items[0]


@router.delete('/{coupon_key}', status_code=204)
def delete_coupon(coupon_key: str):
    coupon_db.delete(key=coupon_key)
    return
