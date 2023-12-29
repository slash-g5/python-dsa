class Solution:
    def search(self, A: list, l: int, h: int, key: int):
        # l: The starting index
        # h: The ending index, you have to search the key in this range
        # Complete this function
        if l > h:
            return -1
        if l == h:
            if A[l] == key:
                return l
            return -1

        if A[l] == key:
            return l
        if A[h] == key:
            return h

        if h == l + 1:
            return -1

        mid = (l + h) // 2

        if A[mid] == key:
            return mid

        if A[h] > A[l]:
            if A[mid] > key:
                return self.search(A, l, mid - 1, key)
            return self.search(A, mid + 1, h, key)

        if self.search(A, l, mid - 1, key) != -1:
            return self.search(A, l, mid - 1, key)

        return self.search(A, mid + 1, h, key)