class SequenceZip:
    def __init__(self, *args):
        self.sequences = args

    def __len__(self):
        if not self.sequences:
            return 0
        return min(len(seq) for seq in self.sequences)

    def __getitem__(self, index):
        return tuple(seq[index] for seq in self.sequences)

    def __iter__(self):
        return iter(self[i] for i in range(len(self)))


sequencezip = SequenceZip('ABC', ['bee', 'geek', 'python'], [1, 2, 3])

print(list(sequencezip))
print(tuple(sequencezip))