class Country:
    country = ('Russia', 'Ukraine', 'Belarus', 'Kazakhstan', 'Other')

    def __iter__(self):
        return iter(self.country)


country_is = Country()
for i in country_is:
    if i == 'Kazakhstan':
        print('Ура, Маша летит в Казахстан!')
