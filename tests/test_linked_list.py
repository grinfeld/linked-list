import unittest

from src.linked_list.linked_list import LinkedList

class MyTestCase(unittest.TestCase):

    def test_something(self):
        ls = LinkedList[int]()
        ls.push(1)
        self.assertEqual(ls.peek_first(), 1)
        self.assertEqual(ls.peek_last(), 1)
        ls.push(2)
        self.assertEqual(ls.peek_first(), 1)
        self.assertEqual(ls.peek_last(), 2)

        expected_reverse_list = []
        for v in ls.reversed_iterator():
            expected_reverse_list.append(v)

        self.assertListEqual(expected_reverse_list, [2, 1])

        last = ls.pop_last()
        self.assertEqual(last, 2)
        self.assertEqual(len(ls), 1)
        self.assertEqual(ls.peek_first(), 1)
        self.assertEqual(ls.peek_last(), 1)

        ls.push(2)
        ls.push(3)
        first = ls.pop_first()
        self.assertEqual(first, 1)
        self.assertEqual(len(ls), 2)
        self.assertEqual(ls.peek_first(), 2)
        self.assertEqual(ls.peek_last(), 3)

if __name__ == '__main__':
    unittest.main()
