import pytest


class PromoLinks:
    promo_list = [
        f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}' \
        for num in range(10)
    ]
    promo_list[7] = pytest.param(promo_list[7], marks=pytest.mark.xfail)