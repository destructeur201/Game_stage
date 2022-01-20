class Response:
    code: int
    message: str
    data: list

    def __init__(self, code = 200, message = "", data = []):
        self.code = code
        self.message = message
        self.data = data

    def json(self):
        return {
            'code': self.code,
            'message': self.message,
            'data': self.data
        }












        