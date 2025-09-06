from __future__ import annotations

from dataclasses import dataclass
from typing import TypeVar, Generic, Iterator, Callable, List, Iterable

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
    add and prepend are O(1)
    pop and peek for first and last element are O(1)
    find element by index O(n)
    """
    def __init__(self):
        self._empty = _EmptyNode()
        self._root = self._empty
        self._last = self._root
        self._size = 0

    def push(self, value: T) -> LinkedList[K]:
        the_last = self._last
        if self._root.is_empty():
            self._root = _Node(value, self._empty, the_last)
            self._last = self._root
        else:
            new_node = _Node(value, self._empty, the_last)
            the_last.next = new_node
            self._last = new_node
            if len(self) == 1:
                self._root = the_last
        self._size = self._size + 1
        return self

    def __iadd__(self, *args, **kwargs):
        return self.push(args[0])

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
        runs over the list immediately as map operation is called
            :param fn - function to transform data of type K to type V
            :return new LinkedList[K] with transformed data
        """
        new_list = LinkedList()
        for v in self:
            new_list.push(fn(v))
        return new_list

    def map_reverse(self, fn: Callable[[T], K]) -> LinkedList[K]:
        """Converts current linked list in reverse order to another transforming data by function
        runs over the list immediately as map_reverse operation is called
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
            self._last.prev.next = self._empty
            self._last = self._last.prev
            self._size = self._size - 1
            return the_last

    def pop_first(self) -> T:
        if self.is_empty():
            return None
        else:
            the_value = self._root.value
            self._root.next.prev = self._empty
            self._root = self._root.next
            self._size = self._size - 1
            if len(self) == 1:
                self._last = self._root
            return the_value

    def get(self, ind: int) -> T:
        """
        Finds the element by its index in the list. For LinkedList, this operation takes O(n)
        :param ind: element in the list
        :return: the element by its index in the list
        :raises IndexError: if index is out of range
        """
        if ind < 0 or ind > self._size-1:
            raise IndexError("Index out of range")
        i = 0
        for v in self:
            if i == ind:
                return v
            i = i + 1
        return None

    def __getitem__(self, *args, **kwargs):
        """
        Finds the element by its index in the list. For LinkedList, this operation takes O(n)
        :param ind: element in the list
        :return: the element by its index in the list
        :raises IndexError: if index is out of range
        """
        return self.get(args[0])

    def set(self, ind: int, value: T) -> LinkedList[K]:
        """
         Sets the element by its index in the list. For LinkedList, this operation takes O(n)
         :param ind: element in the list
         :param value: new value
         :return: the element by its index in the list
         :raises IndexError: if index is out of range
         """
        if ind < 0 or ind > self._size-1:
            raise IndexError("Index out of range")
        i = 0
        for v in self._inner_iter():
            if i == ind:
                v.value = value
                break
            i = i + 1
        return self

    def __setitem__(self, *args, **kwargs):
        return self.set(args[0], args[1])

    def exists(self, value: T) -> bool:
        """
        Checks whether the element exists in the list. For LinkedList, this operation takes O(n)
        :param value: T to test if it exists in the list
        :return: True if element exists and False if it doesn't
        """
        for v in self:
            if v == value:
                return True
        return False

    def aggregate(self, zero: Generic[K], fn: Callable[[T, T], K]) -> Generic[K]:
        agg = zero
        for v in self:
            agg = fn(agg, v)
        return agg

    def sum(self):
        return self.aggregate(0, lambda a, b: a + b)

    def concatenate(self, other: Iterator[K]) -> LinkedList[K]:
        for v in other:
            self.push(v)
        return self

    def filter(self, fn: Callable[[T], bool]) -> LinkedList[K]:
        """ this operation is immediate and not lazy - creates new list """
        new_list = LinkedList()
        for v in self:
            if fn(v):
                new_list.push(v)
        return new_list

    def filter_iter(self, fn: Callable[[T], bool]) -> Iterable[K]:
        node = self._root
        while not node.is_empty():
            if fn(node.value):
                yield node.value
            node = node.next

    def __add__(self, other):
        return self.concatenate(other)

    def __repr__(self) -> str:
        return f"LinkedList({list(self)})"
