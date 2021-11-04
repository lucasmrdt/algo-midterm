class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def fromArray(self, arr):
        sorted_arr = sorted(arr)
        self.root = self._sortedArrayToBST(sorted_arr)

    def fromSortedArray(self, arr):
        self.root = self._sortedArrayToBST(arr)

    def _sortedArrayToBST(self, arr):
        n = len(arr)
        if n == 0:
            return None
        if n == 1:
            return TreeNode(arr[0])
        x = arr[n//2]
        root = TreeNode(x)
        root.left = self._sortedArrayToBST(arr[:n//2])
        root.right = self._sortedArrayToBST(arr[n//2+1:])
        return root

    def __str__(self) -> str:
        output = ""
        q = [self.root]
        i = 0
        while q:
            s = ', '.join(
                [f'{n.val}' for n in q])
            output += f'Depth {i} [{"FULL" if 2**i == len(q) else len(q)}]: {s}\n'
            q_next = []
            for n in q:
                if n.left:
                    q_next.append(n.left)
                if n.right:
                    q_next.append(n.right)
            q = q_next
            i += 1
        return output

    def __repr__(self) -> str:
        return self.__str__()


if __name__ == "__main__":
    import random
    l = [random.randint(0, 100) for _ in range(1000)]
    bst = BST()
    bst.fromArray(l)
    print(bst)
