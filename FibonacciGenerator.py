class FibonacciGenerator:
    def __init__(self):
        self._sequence = [0, 1]
        self._index = -1

    def _get_next(self):
        self._index += 1
        if self._index < 2:
            return self._sequence[self._index]
        self._sequence.append(self._sequence[-1] + self._sequence[-2])
        return self._sequence[-1]

    def generate(self, limit):
        for i in range(limit):
            yield self._get_next()

