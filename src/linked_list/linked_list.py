from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic, Iterator, Callable, List

T = TypeVar('T')

@dataclass
class _Node(Generic[T]):
    value: T
    next: _Node[T] = None
    prev: _Node[T] = None

    def is_empty(self) -> bool:
        return False

@dataclass
class _EmptyNode(_Node[T]):
    def __init__(self):
        super().__init__(None)

    def is_empty(self) -> bool:
        return True

class LinkedList(Generic[T]):
    """
    Class represents 2-direction LinkedList
    """
    def __init__(self):
        self._root = _EmptyNode()
        self._last = _EmptyNode()
        self._size = 0

    def push(self, value: T):
        new_node = _Node(value, _EmptyNode(), self._root)
        if self._root.is_empty():
            self._last = self._root = new_node
        else:
            self._last = _Node(value, _EmptyNode(), self._last)
            if len(self) == 1:
                self._root.next = new_node
        self._size = self._size + 1

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def __iter__(self) -> Iterator[T]:
        for i in self._inner_iter():
            yield i.value

    def _inner_iter(self) -> Iterator[_Node[T]]:
        node = self._root
        while not node.is_empty():
            yield node
            node = node.next

    def reversed_iterator(self) -> Iterator[T]:
        for i in self._inner_reversed_iter():
            yield i.value

    def _inner_reversed_iter(self) -> Iterator[_Node[T]]:
        node = self._last
        while not node.is_empty():
            yield node
            node = node.prev

    def to_list(self) -> List[T]:
        ls = []
        for v in self:
            ls.append(v)
        return ls

    def reverse_list(self)-> List[T]:
        ls = []
        for v in self.reversed_iterator():
            ls.append(v)
        return ls

    K = TypeVar("K")
    def map(self, fn: Callable[[T], K]) -> LinkedList[K]:
        """Converts current linked list to another transforming data by function
            :param fn - function to transform data of type K to type V
            :return new LinkedList[K] with transformed data
        """
        new_list = LinkedList()
        for v in self:
            new_list.push(fn(v))
        return new_list

    def map_reverse(self, fn: Callable[[T], K]) -> LinkedList[K]:
        """Converts current linked list in reverse order to another transforming data by function
            :param fn - function to transform data of type K to type V
            :return new LinkedList[K] with transformed data
        """
        new_list = LinkedList()
        for v in self.reversed_iterator():
            new_list.push(fn(v))
        return new_list

    def peek_first(self) -> T:
        if self.is_empty():
            return None
        else:
            return self._root.value

    def peek_last(self) -> T:
        if self.is_empty():
            return None
        else:
            return self._last.value

    def pop_last(self) -> T:
        if self.is_empty():
            return None
        else:
            the_last = self._last.value
            self._last.prev.next = _EmptyNode()
            self._last = self._last.prev
            self._size = self._size - 1
            return the_last

    def pop_first(self) -> T:
        if self.is_empty():
            return None
        else:
            the_value = self._root.value
            self._root.next.prev = _EmptyNode()
            self._root = self._root.next
            self._size = self._size - 1
            if len(self) == 1:
                self._last = self._root
            return the_value

    def __repr__(self) -> str:
        return f"LinkedList({list(self)})"
