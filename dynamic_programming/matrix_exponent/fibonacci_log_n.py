# calculate fibonacci in log(n)

def fibonacci(n):
    # calculate M**p

    # multiply two matrix
    def multiply(M1, M2):
        res = [[0 for _ in range(len(M2[0]))] for _ in range(len(M1))]
        for i in range(len(M1)):
            for j in range(len(M2[0])):
                res[i][j] = 0
                for k in range(len(M1[0])):
                    res[i][j] += M1[i][k] * M2[k][j]
        return res

    def mat_expo(M, p):
        if p == 0:
            return [[1, 1], [1, 1]]
        if p == 1:
            return M
        if p == 2:
            return multiply(M, M)
        if p % 2 == 0:
            return mat_expo(multiply(M, M), p // 2)
        return multiply(M, mat_expo(M, p - 1))

    if n == 0:
        return 0
    if n == 1:
        return 1

    B = [[1, 1], [1, 0]]
    A2 = [[1], [0]]

    return sum(multiply(mat_expo(B, n-1), A2)[0])


if __name__ == "__main__":
    print(fibonacci(500))
