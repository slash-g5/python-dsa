import copy


def get_blocked_positions(transitions):
    blocked_positions = []
    for transition in transitions:
        blocked_position = transition.direction + transition.position
        blocked_positions.append(blocked_position)
    return blocked_positions


class Transition:
    def __init__(self):
        self.blocked_col = {}
        self.up_diagonal = {}
        self.down_diagonal = {}

    def indexAllowed(self, x, y):
        if (x + y) in self.up_diagonal:
            return False
        if (x - y) in self.down_diagonal:
            return False
        if y in self.blocked_col:
            return False
        return True


class TempAnswer:
    def __init__(self, answer, transitions):
        self.answer = answer
        self.transitions = transitions


class Solution:

    def nQueenHelper(self, current, end, current_answers):

        if current > end:
            return current_answers

        next_answers = []

        if not current_answers:
            for index in range(1, end + 1):
                next_transitions = Transition()
                answer = [index]
                next_transitions.blocked_col[index] = True
                next_transitions.up_diagonal[current + index] = True
                next_transitions.down_diagonal[current - index] = True
                next_answers.append(TempAnswer(answer, next_transitions))
            return self.nQueenHelper(current + 1, end, next_answers)

        for tempAnswer in current_answers:
            answer = tempAnswer.answer
            for index in range(1, end + 1):
                if not tempAnswer.transitions.indexAllowed(current, index):
                    continue
                next_transitions = copy.deepcopy(tempAnswer.transitions)
                next_transitions.blocked_col[index] = True
                next_transitions.up_diagonal[current + index] = True
                next_transitions.down_diagonal[current - index] = True
                temp_next_ans = answer + [index]
                next_answers.append(TempAnswer(temp_next_ans, next_transitions))

        if not next_answers:
            return []

        return self.nQueenHelper(current + 1, end, next_answers)

    def nQueen(self, n):
        # code here
        help_ans = self.nQueenHelper(1, n, [])
        final_ans = []
        for element in help_ans:
            final_ans.append(element.answer)
        return final_ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.nQueen(9))
