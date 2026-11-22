from algorithmic_package.exceptions import UndersizeError


class stack:
    def __init__(self):
        self.items = []


    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.items:
            raise UndersizeError("Нельзя извлечь элемент из пустого стека")
        return self.items.pop()

    def peek(self):
        if not self.items:
            raise UndersizeError("Нельзя посмотреть вершину пустого стека")
        return self.items[-1]


    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return len(self) > 0

    def dup(self):
        self.push(self.peek())


    def swap(self):
        if len(self.items) < 2:
            raise UndersizeError("Недостаточно элементов для swap")
        self.items[-2], self.items[-1] = self.items[-1], self.items[-2]