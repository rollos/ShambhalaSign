class TestClip:

    def __init__(self, delegate, text: str):
        self.delegate = delegate

        self.text = text

    def run(self) -> None:
        for i in range(10):
            print("{}: {}".format(i, self.text))

        self.delegate.finished()
