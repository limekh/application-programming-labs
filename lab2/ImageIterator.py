from read_file import read_file


class ImageIterator:
    def __init__(self, annotation: str):
        self.annotation = read_file(annotation)
        self.counter = 0
        self.limit = len(self.annotation)

    def __iter__(self):
        return self

    def __next__(self) -> str:
        if self.counter >= self.limit:
            raise StopIteration
        else:
            result = self.annotation[self.counter]
            self.counter += 1
            return result
