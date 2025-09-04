import unittest

from src.linked_list.linked_list import LinkedList

class MyTestCase(unittest.TestCase):

    def test_operations_on_non_empty_list(self):
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
        ls.push(4)
        self.assertListEqual(ls.map(lambda k: k + 1).to_list(), [3,4,5])
        self.assertListEqual(ls.map_reverse(lambda k: k + 1).to_list(), [5,4,3])

        self.assertListEqual(ls.map(lambda k: f"{k}").to_list(), ["2","3","4"])
        self.assertListEqual(ls.map_reverse(lambda k: f"{k}").to_list(), ["4","3","2"])

        self.assertEqual(ls.get(0), 2)
        self.assertEqual(ls.get(1), 3)

        self.assertListEqual(ls.reverse_list(), [4,3,2])

        self.assertTrue(ls.exists(3))
        self.assertRaises(IndexError, ls.get, 10)

    def test_operations_on_empty_list(self):
        ls = LinkedList[int]()
        self.assertRaises(IndexError, ls.get, 2)
        self.assertEqual(len(ls), 0)
        self.assertEqual(ls.peek_first(), None)
        self.assertEqual(ls.peek_last(), None)
        self.assertFalse(ls.exists(3))
        self.assertListEqual(ls.to_list(), [])
        self.assertListEqual(ls.map(lambda k: k + 1).to_list(), [])
        self.assertListEqual(ls.map_reverse(lambda k: k + 1).to_list(), [])

if __name__ == '__main__':
    unittest.main()
