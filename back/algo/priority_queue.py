class PriorityQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = [None] * max_size
        self.size = 0

    def insert(self, value):
        if self.size == self.max_size:
            if value > self.data[0]:
                self.data[0] = value
                self._bubble_down_head()
        else:
            i = self.size
            self.data[i] = value
            self.size += 1
            self._bubble_up(i)

    def pop(self):
        if self.size == 0:
            return None
        self.size -= 1
        data = self.data[0]
        self._bubble_down()
        return data

    def _bubble_up(self, i):
        curr = i
        while curr > 0:
            p = self._parent(curr)
            if self.data[p] > self.data[curr]:
                self.data[p], self.data[curr] = self.data[curr], self.data[p]
            curr = p

    def _bubble_down(self):
        i = 0
        prev_i = None
        while i is not None:
            l = self._child_left(i)
            r = self._child_right(i)
            prev_i = i
            if l is None and r is None:
                i = None
            elif l is None:
                self.data[i] = self.data[r]
                i = r
            elif r is None:
                self.data[i] = self.data[l]
                i = l
            else:
                if self.data[l] < self.data[r]:
                    self.data[i] = self.data[l]
                    i = l
                else:
                    self.data[i] = self.data[r]
                    i = r
        if prev_i is not None:
            self.data[prev_i] = None

    def _bubble_down_head(self):
        def update_min(curr, l, r):
            if l is None and r is None:
                return None
            if l is None:
                if self.data[r] < self.data[curr]:
                    self.data[r], self.data[curr] = self.data[curr], self.data[r]
                    return r
                return None
            if r is None:
                if self.data[l] < self.data[curr]:
                    self.data[l], self.data[curr] = self.data[curr], self.data[l]
                    return l
                return None
            if self.data[l] <= self.data[r] and self.data[l] < self.data[curr]:
                self.data[l], self.data[curr] = self.data[curr], self.data[l]
                return l
            if self.data[r] <= self.data[l] and self.data[r] < self.data[curr]:
                self.data[r], self.data[curr] = self.data[curr], self.data[r]
                return r
            return None

        curr = 0
        while curr is not None:
            l = self._child_left(curr)
            r = self._child_right(curr)
            curr = update_min(curr, l, r)

    def _child_left(self, i):
        l = 2 * i + 1
        if l > len(self.data) - 1 or self.data[l] is None:
            return None
        return l

    def _child_right(self, i):
        r = 2 * i + 2
        if r > len(self.data) - 1 or self.data[r] is None:
            return None
        return r

    def _parent(self, i):
        if i == 0:
            return None
        return (i - 1) // 2

    def __str__(self) -> str:
        output = ""
        q = [0]
        i = 0
        while q:
            s = ', '.join([f'{self.data[n]}' for n in q])
            output += f'Depth {i} [{"FULL" if 2**i == len(q) else len(q)}]: {s}\n'
            q_next = []
            for n in q:
                if self._child_left(n):
                    q_next.append(self._child_left(n))
                if self._child_right(n):
                    q_next.append(self._child_right(n))
            q = q_next
            i += 1
        return output

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    # For relative imports to work in Python 3.6
    import os
    import sys
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))

    import random
    k = 10
    p = PriorityQueue(k)
    l = list(range(1000))[::-1]
    for i, el in enumerate(l):
        p.insert(el)
        print(f"\n\nSTEP {i}: insert '{el}'")
        print(p)
    print(f"\n{k}th best: '{','.join([str(p.pop()) for _ in range(k)])}'")
