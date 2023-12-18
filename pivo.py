from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Пожалуйста! У меня нет денег :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Вы не купите мне пива?"
    return msg, say_please


print(say())                 # Вы не купите мне пива?
print(say(say_please=True))  # Вы не купите мне пива? Пожалуйста! У меня нет денег :(
