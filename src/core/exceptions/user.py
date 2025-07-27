class UserException(Exception):
    def __init__(self, message: str):
        self.message = message


class UserIdNotFoundException(UserException):
    def __init__(self, id: int):
        super().__init__(message=f"User {id} not found")


class UserNameNotFoundException(UserException):
    def __init__(self, name: str):
        super().__init__(message=f"User {name} not found")


class UserAlreadyExistsException(UserException):
    def __init__(self, name: str):
        super().__init__(message=f"User {name} Already exists")
