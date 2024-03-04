class KondratyPalich:
    status = 'Деда'


class Vasya(KondratyPalich):
    status = 'Отец'


class Masha(KondratyPalich):
    status = 'Дочь'


masha = Masha()
vasya = Vasya()
print(masha.status, vasya.status, sep='\n')
