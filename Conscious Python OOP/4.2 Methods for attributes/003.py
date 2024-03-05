class OnlyVasya:
    def __setattr__(self, key, value):
        if key == 'name':
            object.__setattr__(self, key, 'Vasya')
            return
        super().__setattr__(key, value)


obj = OnlyVasya()
obj.name = 'Masha'
print(getattr(obj, 'name'))
