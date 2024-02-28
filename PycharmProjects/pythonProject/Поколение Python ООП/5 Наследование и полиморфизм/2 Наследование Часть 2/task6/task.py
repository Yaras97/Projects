class FieldTracker:
    def __setattr__(self, key, value):
        if key not in self.__dict__:
            self.__dict__.setdefault('cache', {})[key] = value
        super().__setattr__(key, value)

    def base(self, attr):
        return self.cache.get(attr)

    def has_changed(self, attr):
        return self.cache.get(attr) != getattr(self, attr)

    def changed(self):
        return {k: v for k, v in self.cache.items() if self.has_changed(k)}

    def save(self):
        self.cache = {k: getattr(self, k) for k in self.cache}