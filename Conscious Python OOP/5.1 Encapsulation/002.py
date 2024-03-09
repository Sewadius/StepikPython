from accessify import private


class Teleport:
    @private
    def __activator_teleport(self):
        print('Активатор от телепорта у Машеньки под подушкой')

    def mama_help(self):
        return self.__activator_teleport()


vasya = Teleport()
vasya.mama_help()
