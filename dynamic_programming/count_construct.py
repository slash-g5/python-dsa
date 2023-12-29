def count_construct_mem(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target == "":
        return 1
    if target in memo:
        return memo[target]
    ans = 0
    for word in word_bank:
        if target.startswith(word):
            cut_string = target[len(word):]
            ans += count_construct_mem(cut_string, word_bank, memo)
    memo[target] = ans
    return ans


def count_construct_tab(target, word_bank):
    dp_array = [0 for _ in range(len(target) + 1)]
    if target == "":
        return 1
    dp_array[0] = 1
    for i in range(1, len(target) + 1):
        curr_string = target[:i]
        for word in word_bank:
            if len(word) > i:
                continue
            if curr_string.endswith(word):
                dp_array[i] += dp_array[i - len(word)]
    return dp_array[len(target)]


if __name__ == "__main__":
    print(count_construct_mem("absbdbd", ["a", "b", "s", "d", "abs", "bd"]))
    print(count_construct_tab("absbdbd", ["a", "b", "s", "d", "abs", "bd"]))
