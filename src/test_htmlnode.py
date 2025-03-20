import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)
    
    def test_ne(self):
        node1 = HTMLNode("p", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)
        