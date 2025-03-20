import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("Text node #1", TextType.CODE)
        node2 = TextNode("Text node #2", TextType.IMAGE)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
