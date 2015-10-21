from unittest import TestCase
from reverse_list import reverse_list
from linkedlist.linked_list import Node


ll = Node(1)
ll.add(2)
ll.add(3)
ll.add(4)

rll = Node(4)
rll.add(3)
rll.add(2)
rll.add(1)

class TestReverseList(TestCase):

    def test_reverse_list(self):
        self.assertEquals(rll, reverse_list(ll))
