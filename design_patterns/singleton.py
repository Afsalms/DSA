class Single(object):
    _instance = None

    def __new__(self):
        if self._instance is None:
            self._instance = super().__new__(self)
        self.test = "test"
        return self._instance



a = Single()

print(id(a))

print(a.test)
a.test = "new test"


b = Single()

print(id(b))

print(b.test)
