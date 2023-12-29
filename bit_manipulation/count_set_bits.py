def getNoOfBits(n):
    if n // 2 == 0:
        return 1
    ans = 1
    while n // 2 != 0:
        n = n // 2
        ans += 1
    return ans


def countSetBits(n):
    # code here
    # return the count
    # 1 => 1
    # 2 => 3
    # 3 => 2 ** n
    if n == 1:
        return 1

    ans = 0

    x = getNoOfBits(n)
    temp = 1
    total_this_count = 0

    for i in range(0, x):
        if i == x-1:
            ans += total_this_count + 1
        this_count = total_this_count + temp
        total_this_count += this_count
        if n % 2 != 0:
            ans += this_count
        n = n // 2
        temp = 2 * temp  # temp = 2**x

    return ans


if __name__ == "__main__":
    countSetBits(8)
