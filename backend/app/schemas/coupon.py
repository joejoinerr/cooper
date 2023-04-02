from __future__ import annotations

import datetime

from pydantic import BaseModel


class CouponBase(BaseModel):
    brand: str
    code: str
    expiry: datetime.datetime
    tags: set[str] = set()


class CouponCreate(CouponBase):
    ...


class CouponUpdate(CouponBase):
    ...


class CouponInDBBase(CouponBase):
    key: str


class Coupon(CouponInDBBase):
    ...


class CouponInDB(CouponInDBBase):
    ...


class CouponList(BaseModel):
    coupons: list[Coupon]
