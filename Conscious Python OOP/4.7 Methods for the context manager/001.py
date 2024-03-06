planets = ['Сатурн', 'Юпитер', 'Земля', 'Марс']


class StarTravel:
    def __init__(self, other: str):
        planets.append(other)

    def __enter__(self):
        return planets

    def __exit__(self, exc_type, exc_value, traceback):
        print('Венера')


with StarTravel('Плутон') as word:
    [print(i) for i in word]
