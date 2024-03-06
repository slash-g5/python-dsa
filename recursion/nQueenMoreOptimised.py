
class Solution:

    def is_valid_state(self, state):
        blocked_col = set()
        blocked_up_dig = set()
        blocked_low_dig = set()
        for i in range(len(state)):
            if state[i] in blocked_col:
                return False
            if state[i] + i in blocked_low_dig:
                return False
            if state[i] - i in blocked_up_dig:
                return False
            blocked_col.add(state[i])
            blocked_up_dig.add(state[i] - i)
            blocked_low_dig.add(state[i] + i)
        return True

    def get_candidates(self, state, n):
        result = []
        for i in range(1, n + 1):
            if self.is_valid_state(state + [i]):
                result.append(state + [i])
        return result


    def nQueen(self, n):
        # code here
        help_ans = self.nQueenHelper(1, n)
        final_ans = []
        for element in help_ans:
            final_ans.append(element.answer)
        return final_ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.nQueen(1))
