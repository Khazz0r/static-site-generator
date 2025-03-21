import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node1 = HTMLNode("p", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        node2 = HTMLNode("p", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        self.assertEqual(node1, node2)
    
    def test_ne(self):
        node1 = HTMLNode("p", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        node2 = HTMLNode("h1", "hello there", ["object1", "object2"], {"href": "https://www.google.com"})
        self.assertNotEqual(node1, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com", "class": "highlight"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" class="highlight">Click me!</a>')
    
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(value="Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_leaf_to_html_no_dict(self):
        node = LeafNode("p", "Click me!", ["href", "highlight"])
        self.assertEqual(node.to_html(), "<p>Click me!</p>")
        