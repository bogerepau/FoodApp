from functools import wraps


def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("IsAdmin!")
        return func(*args, **kwargs)
    return wrapper