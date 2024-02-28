from time import perf_counter


class AdvancedTimer:
    def __init__(self):
        self.last_run = None
        self.runs = []
        self.min = None
        self.max = None

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.runs.append(perf_counter() - self.start)
        self.last_run = self.runs[-1]
        self.min = min(self.runs)
        self.max = max(self.runs)


timer = AdvancedTimer()

print(timer.runs)
print(timer.last_run)
print(timer.min)
print(timer.max)