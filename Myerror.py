class Error(Exception):
    pass


class ValueTooLargeError(Error):
    # Введенно слишком большое значение
    pass


class ValueTooSmallError(Error):
    # Введенно слишком маленькое значение
    pass


class WrongdataTypeError(Error):
    # Введен неверный формат данных
    pass
