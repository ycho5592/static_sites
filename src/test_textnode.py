import unittest

from textnode import TextNode, TextType, text_node_to_html_node, split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("what is this", TextType.BOLD, "htts://www.boot.dev")
        node2 = TextNode("what is this", TextType.ITALIC, "htts://www.boot.dev")
        self.assertNotEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.LINKS, "htts://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.LINKS, "htts://www.boot.dev")
        self.assertEqual(node, node2)
    
    def test_not_eq2(self):
        node = TextNode("what is this", TextType.BOLD, "htts://www.boot.dev")
        node2 = TextNode("what is this", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[1].text, "bolded")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_delim_code(self):
        node = TextNode("This is `code` block", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def test_delim_italic(self):
        node = TextNode("Words *italics* more words", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)

    def test_unclosed_delim(self):
        node = TextNode("This has an **unclosed bold", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_multiple_nodes(self):
        node1 = TextNode("Text with `code`", TextType.TEXT)
        node2 = TextNode("Already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)


if __name__ == "__main__":
    unittest.main()