class AlgorithmError(Exception):
    pass


class DeepRecursionError(AlgorithmError):
    pass


class NegativeNumberError(AlgorithmError):
    pass


class NotAnInteger(AlgorithmError):
    pass


class invalidDataTypeError(AlgorithmError):
    pass


class UndersizeError(AlgorithmError):
    pass