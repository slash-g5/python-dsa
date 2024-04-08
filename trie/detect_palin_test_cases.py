import random
import detect_palin_pairs


def generate_test_case(length):
    """
    Generates a test case where a pair of strings exists in an array,
    such that the sum of the strings is a palindrome.

    Args:
    length (int): Length of the array

    Returns:
    tuple: A tuple containing the array of strings and the pair of indices
    """
    # Generate random strings of random lengths
    strings = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))) for _ in range(length)]

    strings = list(set(strings))

    # Find a pair of strings such that their sum is a palindrome
    pair_indices = None
    length = len(strings)
    for i in range(len(strings)):
        for j in range(i + 1, length):
            if is_palindrome(strings[i] + strings[j]):
                pair_indices = (i, j)
                break
            if is_palindrome(strings[j] + strings[i]):
                pair_indices = (j, i)
                break
        if pair_indices:
            break

    return strings, pair_indices


def is_palindrome(s):
    """
    Checks if a string is a palindrome.

    Args:
    s (str): The input string

    Returns:
    bool: True if the string is a palindrome, False otherwise
    """
    return s == s[::-1]


# Example usage
if __name__ == "__main__":
    j = 0
    array_length = 10
    positiveCount = 0
    negativeCount = 0
    error_count = 0
    for i in range(5000000):
        print(i)
        test_case = generate_test_case(array_length)
        res = detect_palin_pairs.search_palindromes(test_case[0])
        if test_case[1] is not None and res == 0:
            print("ERROR NOT NONE")
            print(f"FAILED {test_case[0]}")
            error_count += 1
        if test_case[1] is None and res == 1:
            print("ERROR")
            print(f"FAILED {test_case[0]}")
            error_count += 1
        if test_case[1] is not None and res == 1:
            positiveCount += 1
        if test_case[1] is None and res == 0:
            negativeCount += 1
    print(f'positive count {positiveCount}')
    print(f'negative count {negativeCount}')
    print(f'error count {error_count}')
