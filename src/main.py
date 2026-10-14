from textnode import TextNode
from textnode import TextType

def main():
    test_node = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(test_node)

main()