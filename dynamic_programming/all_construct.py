def all_construct_mem(target, word_bank, memo=None):
    if not memo:
        memo = {}
    if target == "":
        memo[target] = []
        return []
    ans = []
    for word in word_bank:
        if target.startswith(word):
            if target == word:
                ans.extend([[word]])
                continue
            sub_ans = all_construct_mem(target[len(word):], word_bank, memo)
            if sub_ans:
                curr_ans = []
                for s in sub_ans:
                    s.append(word)
                    curr_ans.append(s)
                ans.extend(curr_ans)

    memo[target] = ans
    return ans


def all_construct_tab(target, word_bank):
    dp_array = [[] for _ in range(len(target) + 1)]
    for i in range(1, len(target) + 1):
        curr_string = target[:i]
        for word in word_bank:
            if len(word) > i:
                continue
            if curr_string.endswith(word):
                if word == curr_string:
                    dp_array[i].extend([[word]])
                    continue
                if not dp_array[i - len(word)]:
                    continue
                for array in dp_array[i-len(word)]:
                    dp_array[i].append(array + [word])

    return dp_array[len(target)]


if __name__ == "__main__":
    print(all_construct_mem("absbdbd", ["a", "b", "s", "d", "abs", "bd"]))
    print(all_construct_tab("absbdbd", ["a", "b", "s", "d", "abs", "bd"]))
