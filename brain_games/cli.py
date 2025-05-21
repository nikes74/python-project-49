import prompt


def get_user_name() -> str:
    name = prompt.string('May I have your name? ')
    return name


def welcome_user() -> object:
    name: str = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
