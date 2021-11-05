class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None
        self.size = 0

    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next
        return l

    def insert(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            self.size += 1
            return

        new_node = Node(data, self.head)
        self.size += 1
        self.head = new_node

    def insert_unique(self, data):
        node = self.head
        while node:
            if node.data == data:
                node.data = data
                return
            node = node.next
        self.insert(data)

    def iter(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __str__(self) -> str:
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next

        ll_string += " None"
        return ll_string

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    print("basic ll:")
    print(ll)

    class Test:
        def __init__(self, data):
            self.data = data

        def __str__(self):
            return str(self.data)

        def __repr__(self):
            return self.__str__()

        def __eq__(self, o: object) -> bool:
            return self.data == o.data

        def __hash__(self) -> int:
            return hash(self.data)

    ll = LinkedList()
    ll.insert(Test(1))
    ll.insert(Test(2))
    ll.insert(Test(3))
    ll.insert_unique(Test(2))
    ll.insert_unique(Test(1))
    print("advanced ll:")
    print(ll)
