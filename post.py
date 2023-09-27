class post:
    def __init__(self, text: str, user: str, comments: dict):
        self.user = user
        self.text = text
        self.comments = comments