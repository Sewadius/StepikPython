class ReadingAccelerator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        result *= 3
        return result


@ReadingAccelerator
def masha_reading(page_number):
    return page_number


print(masha_reading(5))
