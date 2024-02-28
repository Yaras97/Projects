from functools import total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        self.version = [int(i) for i in version.split('.')]
        self.version += [0] * (3 - len(self.version))

    def __str__(self):
        return '.'.join(map(str, self.version))

    def __repr__(self):
        return f"Version('{'.'.join(map(str, self.version))}')"

    def __eq__(self, other):
        if isinstance(other, Version):
            return self.version == other.version
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return self.version < other.version
        return NotImplemented

print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))