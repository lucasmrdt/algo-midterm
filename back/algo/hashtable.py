from .linked_list import LinkedList


class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __hash__(self) -> int:
        return hash(self.key)

    def __eq__(self, o: object) -> bool:
        return isinstance(o, HashTableNode) and self.key == o.key

    def __repr__(self) -> str:
        return f"([{self.key}]=>'{self.value}')"


class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = [LinkedList() for _ in range(size)]

    def hashfunction(self, key):
        return hash(key) % self.size

    def put(self, key, data):
        hashvalue = self.hashfunction(key)
        bucket = self.buckets[hashvalue]
        node = HashTableNode(key, data)
        bucket.insert_unique(node)

    def get(self, key):
        hashvalue = self.hashfunction(key)
        bucket = self.buckets[hashvalue]
        for element in bucket.iter():
            if element.data.key == key:
                return element.data.value
        return None

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __str__(self) -> str:
        return '\n'.join(str(b) for b in self.buckets)

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    ht = HashTable()
    k = 25
    for i in range(k):
        ht.put(f"test{i}", i)
    print(ht)
    for i in range(k):
        print(ht.get(f"test{i}"))
