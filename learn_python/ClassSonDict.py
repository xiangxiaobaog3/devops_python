
class DistinctError(ValueError):

class distinctdict(dict):

    def __setitem__(self, key, value):
        if value in self.values():
            if (
                    (key in self and self[key] != value) or
                    key not in self):
                raise DistinctError("This value already exists for different key")

        super().__setitem__(key, value)
