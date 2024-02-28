class EasyDict(dict):
    def __getattr__(self, item):
        return super().__getitem__(item)


