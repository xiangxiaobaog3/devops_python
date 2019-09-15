class User:
    def __new__(cls, *args, **kwargs):
        print("in new")
        return super().__new__(cls)
    def __init__(self, name):
        print("in init")
        self.name = name

if __name__ == "__main__":
    user = User(name="bobby")