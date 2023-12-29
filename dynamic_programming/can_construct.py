# "abcdef" ["abc","def"] => true
# "lokikik" ["lok" , "ki" , "ki"] => false
# can the string target be derived by concatenating strings from word bank(repeating same word is allowed)
import time


def can_construct_rec(target, word_bank):
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            if can_construct_rec(target[len(word):], word_bank):
                return True
    return False


def can_construct_mem(target, word_bank, mem=None):
    if mem is None:
        mem = {}
    if target == "":
        return True
    if target in mem:
        return mem[target]
    for word in word_bank:
        if target.startswith(word):
            cut_string = target[len(word):]
            if can_construct_mem(cut_string, word_bank, mem):
                mem[target] = True
                return True

    mem[target] = False
    return False


def print_elapsed(start_time):
    elapsed_time = time.time() - start_time
    print(f"Time taken: {elapsed_time} seconds")


def perform_rec_test():
    print("performing recursion test")
    start_time = time.time()
    print(can_construct_rec("abcdef", ["abc", "def"]))
    print_elapsed(start_time)
    start_time = time.time()
    print(can_construct_rec("lokikik", ["lok", "ki", "ki"]))
    print_elapsed(start_time)
    start_time = time.time()
    print(can_construct_rec(s, ["e", "ee", "eee", "eeee", "a", "b", "c", "ccc"]))
    print_elapsed(start_time)


def perform_mem_test():
    print("performing mem test")
    start_time = time.time()
    print(can_construct_mem("abcdef", ["abc", "def"]))
    print_elapsed(start_time)
    start_time = time.time()
    print(can_construct_mem("eeef", ["e", "ee"]))
    print_elapsed(start_time)
    start_time = time.time()
    print(can_construct_mem(s, ["e", "ee", "eee", "eeee", "a", "b", "c", "ccc"]))
    print_elapsed(start_time)


if __name__ == "__main__":
    s = ["e" for _ in range(25)]
    s = "".join(s)
    s += "zz"
    perform_rec_test()
    perform_mem_test()
