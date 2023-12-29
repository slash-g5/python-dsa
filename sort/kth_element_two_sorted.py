

def KthElementHelper(arr1, arr2, l1, r1, l2, r2, k):
    if l2 > r2:
        return arr1[l1 + k]

    if l1 > r1:
        return arr2[l2 + k]

    if k == 0:
        if l1 > r1 and l2 > r2:
            return min(arr1[l1], arr2[l2])
        if l2 > r2:
            return arr1[l1]
        return arr2[l2]

    if k == 1:
        if arr1[l1] > arr2[l2]:
            if l2 + 1 <= r2:
                return min(arr1[l1], arr2[l2 + 1])
            return arr1[l1]
        else:
            if l1 + 1 <= r1:
                return min(arr1[l1 + 1], arr2[l2])
            return arr2[l2]

    if l1 + k // 2 > r1:
        m1_temp = r1
    else:
        m1_temp = l1 + k // 2

    if l2 + k // 2 > r2:
        m2_temp = r2
    else:
        m2_temp = l2 + k // 2

    if arr1[m1_temp] > arr2[m2_temp]:
        return KthElementHelper(arr1, arr2, l1, r1, m2_temp + 1, r2, k - m2_temp + l2 - 1)

    else:
        return KthElementHelper(arr1, arr2, m1_temp + 1, r1, l2, r2, k - m1_temp + l1 - 1)


class Solution:
    def kthElement(self, arr1, arr2, n, m, k):
        return KthElementHelper(arr1, arr2, 0, n - 1, 0, m - 1, k - 1)


# {
# Driver Code Starts
# Initial Template for Python 3

def main():
    T = int(input())

    while (T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends