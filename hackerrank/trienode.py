class TrieNode:
    """
        Simplified version of https://en.wikipedia.org/wiki/Trie
        for the sake of https://www.hackerrank.com/challenges/ctci-contacts/problem
    """
    def __init__(self, value):
        self.children = {}      # mapping from character ==> Node
        self.value = value      # sort of compression to keep remaining of string
                                # instead of creation of new Node for each of them
                                # may use slots to save memory

        self.cnt = 1

        self.__repr__ = self.__str__

    def __str__(self):
        attr_list = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
        str_repr = "["
        for every_attr in attr_list:
            str_repr += every_attr + " - " + str(getattr(self, every_attr)) + " "

        str_repr += "]"

        return str_repr

    def extend(self):
        if not self.value:
            return
        self.children[self.value[0]] = TrieNode(self.value[1:])
        self.value = None


def insert(root, some_string):
    node = root

    for idx, char in enumerate(some_string):
        if char in node.children:
            node = node.children[char]
            node.cnt += 1
            node.extend()
        else:
            node.children[char] = TrieNode(some_string[idx+1:])
            break


def find(node, prefix):

    for char in prefix:
        if char in node.children:
            node = node.children[char]
            node.extend()
        else:
            return 0
    return node.cnt


def check_test_case(multiline_input_string):
    n = int(multiline_input_string)

    for n_itr in xrange(n):
        opContact = multiline_input_string.split()

        op = opContact[0]

        contact = opContact[1]

        if op == 'add':
            insert(root, contact)
        elif op == 'find':
            print find(root, contact)


if __name__ == '__main__':

    root = TrieNode("")

    insert(root, "hack")
    insert(root, "hackerank")
    insert(root, "her")
    insert(root, "ham")
    insert(root, "hum")

    print find(root, "hac")
    print find(root, "ha")
    print find(root, "h")
    print find(root, "hu")
