from unittest import TestCase
from linked_list import Node

class TestLinkedList(TestCase):

    def test_empty_list(self):
        self.assertEqual(None, Node()._next)
        self.assertEqual(None, Node()._value)

    def test_single_element(self):
        self.assertEquals(1, Node(1)._value)
        self.assertEquals('1', str(Node(1)))

    def test_two_elements(self):
        ll = Node(1)
        ll.add(2)
        self.assertEquals(2, ll._next._value)
        self.assertEquals("1, 2", str(ll))

    def test_three_elemets(self):
        ll = Node(1)
        ll.add(2)
        ll.add(3)

        self.assertEquals(1, ll.head())
        self.assertEquals(3, ll.tail())
        self.assertEquals(3, ll.length())
        self.assertEquals("1, 2, 3", str(ll))

        ll2 = Node(-1)
        ll2.add(10)
        ll2.add(5)
        ll2.add(4)
        ll2.add(9)

        self.assertEquals(-1, ll2.head())
        self.assertEquals(9, ll2.tail())
        self.assertEquals(5, ll2.length())
        self.assertEquals("-1, 10, 5, 4, 9", str(ll2))

