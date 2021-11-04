import hashlib


def hashFunction1(x: str):
    h = hashlib.sha256(x.encode())
    return int(h.hexdigest(), base=16)


def hashFunction2(x: str):
    h = hashlib.sha512(x.encode())
    return int(h.hexdigest(), base=16)


def hashFunction3(x: str):
    h = hashlib.md5(x.encode())
    return int(h.hexdigest(), base=16)


class BloomFilter:
    def __init__(self, m=20, hashFunctions=[hashFunction1, hashFunction2, hashFunction3]):
        self.m = m
        self.n = 0
        self.k = len(hashFunctions)
        self.vector = [0] * m
        self.falsePositive = 0
        self.hashFunctions = hashFunctions

    def insert(self, value):
        h = str(hash(value))
        self.n += 1
        self.falsePositive = (1 - (1 - 1/self.m)**(self.n*self.k))**self.k
        for hashFun in self.hashFunctions:
            hashValue = hashFun(h) % self.m
            self.vector[hashValue] = 1

    def contains(self, value):
        h = str(hash(value))
        for hashFun in self.hashFunctions:
            hashValue = hashFun(h) % self.m
            if self.vector[hashValue] == 0:
                return 0
        return 1-self.falsePositive


if __name__ == '__main__':
    bf = BloomFilter()
    bf.insert('a')
    bf.insert('b')
    bf.insert('c')
    bf.insert('d')
    print("Contains 'a' ? %f" % bf.contains('a'))
    print("Contains 'b' ? %f" % bf.contains('b'))
    print("Contains 'c' ? %f" % bf.contains('c'))
    print("Contains 'd' ? %f" % bf.contains('d'))
    print("Contains 'e' ? %f" % bf.contains('e'))
    print("Contains 'f' ? %f" % bf.contains('f'))
    print("Contains 'g' ? %f" % bf.contains('g'))
    print("Contains 'h' ? %f" % bf.contains('h'))
    print("Contains 'i' ? %f" % bf.contains('i'))
    print("Contains 'j' ? %f" % bf.contains('j'))
    print("Contains 'k' ? %f" % bf.contains('k'))
    print("Contains 'l' ? %f" % bf.contains('l'))
    print("Contains 'm' ? %f" % bf.contains('m'))
    print("Contains 'n' ? %f" % bf.contains('n'))
