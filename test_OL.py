import unittest

from numpy import False_
from OL import OrderedList
from OL import Node
import random
class MyTests(unittest.TestCase):

    def test_find(self):
        n = OrderedList(False)
        for i in range(100):
            n.add(random.randint(0,100))
        array =  n.get_all()
        for i in range(100):
            self.assertEqual(n.find(array[i]),array[i])

    def test_del(self):
        n = OrderedList(False)
        for i in range(100):
            n.add(random.randint(0,100))
        for i in range(100):
            n.delete(random.randint(0,100))
        self.assertEqual(n.len(),0)

    def test_add(self):
        ...

    ...

if __name__ == '__main__':
    unittest.main()