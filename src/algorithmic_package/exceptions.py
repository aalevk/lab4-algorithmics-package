class AlgorithmError(Exception):
    pass


class DeepRecursionError(AlgorithmError):
    pass


class NegativeNumberError(AlgorithmError):
    pass


class NotAnInteger(AlgorithmError):
    pass


class InvalidDataTypeError(AlgorithmError):
    pass


class UndersizeError(AlgorithmError):
    pass