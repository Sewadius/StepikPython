class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
setattr(Goods, 'inflation', 100)
print(getattr(Goods, 'price'), getattr(Goods, 'inflation'))
