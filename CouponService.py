class CouponService:

    COUPONS = {
        "SAVE50": 50,
        "SAVE100": 100,
        "NEWUSER": 150
    }

    @staticmethod
    def apply_coupon(code, subtotal):
        if code in CouponService.COUPONS:
            discount = CouponService.COUPONS[code]
            return min(discount, subtotal)
        return 0
