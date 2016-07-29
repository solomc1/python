class Counter:
    def __init__(self):
        self._count = 0

    def count(self):
        self._count += 1
        return self._count

    def reset(self):
        self._count = 0
