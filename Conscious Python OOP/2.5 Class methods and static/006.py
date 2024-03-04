from datetime import datetime


class Product:
    TEXT_1 = 'Срок годности в порядке'
    TEXT_2 = 'Срок годности истёк'

    @staticmethod
    def check_date(today, expiry) -> None:
        start = datetime.strptime(today, "%Y-%m-%d")
        finist = datetime.strptime(expiry, "%Y-%m-%d")
        print(Product.TEXT_1 if finist > start else Product.TEXT_2)


today_date = "2024-01-12"
expiry_date1 = "2024-01-31"
expiry_date2 = "2024-01-1"
expiry_date3 = "2024-01-12"

Product.check_date(today_date, expiry_date1)
Product.check_date(today_date, expiry_date2)
Product.check_date(today_date, expiry_date3)
