# ./main.sh
from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", TextType.BOLD, "htts://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()

