import unittest

from numpy import False_
from OL import OrderedList
from OL import Node
import random
class MyTests(unittest.TestCase):
    def test_find(self):
        n = OrderedList(False)
        self.assertEqual(None,n.find(0))
        for i in range(random.randint(0,1000)):
            n.add(random.randint(0,1000))
        for i in range(random.randint(0,1000)):
            n.find(random.randint(0,1000))
        n1 = OrderedList(True)
        self.assertEqual(None,n1.find(0))
        for i in range(random.randint(0,1000)):
            n1.add(random.randint(0,1000))
        for i in range(random.randint(0,1000)):
            n1.find(random.randint(0,1000))

    def test_del(self):
        n = OrderedList(False)
        n.add(50)
        n.add(51)
        n.delete(50)
        self.assertEqual(n.len(),1)
        n.delete(51)
        self.assertEqual(n.len(),0)
        for i in range(100):
            n.add(i)
        for i in range(100):
            n.delete(i)
        self.assertEqual(n.len(),0)

        n1 = OrderedList(False)
        n1.add(50)
        n1.add(51)
        n1.delete(50)
        self.assertEqual(n1.len(),1)
        n1.delete(51)
        self.assertEqual(n1.len(),0)
        for i in range(100):
            n1.add(i)
        for i in range(100):
            n1.delete(i)
        self.assertEqual(n1.len(),0)

    def test_add(self):
        n = OrderedList(False)
        for i in range(random.randint(0,1000)):
            n.add(random.randint(0,1000))
        n1 = OrderedList(False)
        for i in range(random.randint(0,1000)):
            n1.add(random.randint(0,1000))

if __name__ == '__main__':
    unittest.main()