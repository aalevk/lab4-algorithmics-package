import pytest

from algorithmic_package.exceptions import UndersizeError
from algorithmic_package.stack import stack


def test_push_and_pop():
    items = stack()
    assert len(items) == 0
    assert not items

    items.push(0)
    assert items
    items.push(20)

    assert len(items) == 2
    assert items.pop() == 20
    assert items.pop() == 0
    assert not items


def test_peek():
    items = stack()
    items.push(10)

    assert items.peek() == 10
    assert len(items) == 1


def test_dup():
    items = stack()
    items.push(10)
    items.dup()

    assert len(items) == 2
    assert items.pop() == 10
    assert items.pop() == 10


def test_swap():
    items = stack()
    items.push(10)
    items.push(20)
    items.push(30)
    items.swap()

    assert len(items) == 3
    assert items.pop() == 20
    assert items.pop() == 30
    assert items.pop() == 10


def test_empty_stack():
    items = stack()

    with pytest.raises(UndersizeError):
        items.pop()
    with pytest.raises(UndersizeError):
        items.peek()
    with pytest.raises(UndersizeError):
        items.dup()
    with pytest.raises(UndersizeError):
        items.swap()


def test_swap_one_item():
    items = stack()
    items.push(10)

    with pytest.raises(UndersizeError):
        items.swap()

    assert items.peek() == 10
    assert len(items) == 1
