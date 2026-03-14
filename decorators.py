
def bold(func):
    def wrapper(text: str):
        text = f'<b>{text}</b>'
        return func(text)
    return wrapper


def italic(func):
    def wrapper(text: str):
        text = f'<i>{text}</i>'
        return func(text)
    return wrapper


@italic
@bold
def matn(text: str) -> str:
    return text

text = matn('salom')
print(text)
