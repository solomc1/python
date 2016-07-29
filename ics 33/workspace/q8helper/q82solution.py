from bag import Bag
import unittest   #use unittest.TestCase
import random     #use random.shuffle, random.randint


class Test_Bag(unittest.TestCase):
    def setUp(self):
        self.alist = ['d','a','b','d','c','b','d']
        self.bag = Bag(self.alist)
        
    def test_len(self):
        self.assertEqual(len(self.bag), 7)
        for i in range(len(self.bag)):
            self.bag.remove(self.alist[0])
            self.alist.pop(0)
            random.shuffle(self.alist)
            self.assertEqual(len(self.bag), 7-(i+1))
            
    def test_unique(self):
        self.assertEqual(self.bag.unique(), 4)
        for i in range (len(self.bag)):
            self.bag.remove(self.alist[0])
            self.alist.pop(0)
            random.shuffle(self.alist)
            self.assertEqual(self.bag.unique(), len(set(self.alist)))
            
    def test_contains(self):
        self.assertIn('a', self.bag)
        self.assertIn('b', self.bag)
        self.assertIn('c', self.bag)
        self.assertIn('d', self.bag)
        self.assertNotIn('x', self.bag)
        
    def test_count(self):
        self.assertEqual(self.bag.count('a'),1)
        self.assertEqual(self.bag.count('b'),2)
        self.assertEqual(self.bag.count('c'),1)
        self.assertEqual(self.bag.count('d'),3)
        self.assertEqual(self.bag.count('x'),0)
        for i in range(len(self.bag)):
            self.bag.remove(self.alist[0])
            self.alist.pop(0)
            random.shuffle(self.alist)
            sum_num = 0
            for v in self.bag.counts.values():
                sum_num+=v
            self.assertEqual(sum_num, 7-(i+1))
            
    def test_eq(self):
        bag2 = []
        for i in range(0,1000):
            bag2.append((random.randint(1,10)))
        check_bag = Bag(bag2)
        random.shuffle(bag2)
        check_bag2 = Bag(bag2)
        self.assertEqual(check_bag,check_bag2)
        check_bag.remove(bag2[0])
        self.assertNotEqual(check_bag,check_bag2)
    
    def test_add(self):
        bag2 = []
        for i in range(0,1000):
            bag2.append((random.randint(1,10)))
        check_bag = Bag(bag2)
        check_bag2 = Bag()
        random.shuffle(bag2)
        for i in check_bag:
            check_bag2.add(i)
        self.assertEqual(check_bag,check_bag2)
            
    def test_remove(self):
        bag2 = []
        for i in range(0,1000):
            bag2.append((random.randint(1,10)))
        check_bag = Bag(bag2)
        self.assertRaises(ValueError, check_bag.remove,21)
        check_bag2 = Bag(bag2)
        for i in bag2:
            check_bag2.add(i)
        for i in bag2:
            check_bag2.remove(i)
        self.assertEqual(check_bag,check_bag2)
        
        
        
            
                        
                         
        