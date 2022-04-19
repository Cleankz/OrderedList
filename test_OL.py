import unittest

from numpy import False_
from OL import OrderedList
from OL import Node
import random
class MyTests(unittest.TestCase):

    def test_del(self):
        n = OrderedList(False)
        n.add(50)
        n.add(51)
        n.delete(50)
        self.assertEqual(n.len(),1)
        for i in range(100):
            n.add(random.randint(0,100))
        for i in range(100):
            n.delete(random.randint(0,100))
        self.assertEqual(n.len(),1)

    def test_add(self):
        ...

if __name__ == '__main__':
    unittest.main()