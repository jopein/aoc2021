class Pretty:

    is_on: bool

    def __init__(self, is_on: bool):
        self.is_on = is_on

    def print(self, msg: str) -> None:
        if self.is_on:
            print(msg)
