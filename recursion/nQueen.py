def get_blocked_positions(transitions):
    blocked_positions = []
    for transition in transitions:
        blocked_position = transition.direction + transition.position
        blocked_positions.append(blocked_position)
    return blocked_positions


class Transition:
    def __init__(self, position, direction):
        self.direction = direction
        self.position = position

    def is_next_possible(self, end):
        if self.direction + self.position < 1:
            return False
        if self.direction + self.position > end:
            return False
        return True

    def next_step(self):
        self.position = self.direction + self.position


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
                next_transitions = []
                answer = []
                answer.append(index)
                next_transitions.append(Transition(index, -1))
                next_transitions.append(Transition(index, 0))
                next_transitions.append(Transition(index, 1))
                next_answers.append(TempAnswer(answer.copy(), next_transitions.copy()))
            return self.nQueenHelper(current + 1, end, next_answers)

        for tempAnswer in current_answers:
            answer = tempAnswer.answer
            transitions = tempAnswer.transitions

            next_transitions = []

            blocked_positions = get_blocked_positions(transitions)

            for transition in transitions:
                if transition.is_next_possible(end):
                    transition.next_step()
                    next_transitions.append(transition)

            for index in range(1, end + 1):
                if index in blocked_positions:
                    continue
                start_length = len(answer)
                answer.append(index)
                next_transitions.append(Transition(index, -1))
                next_transitions.append(Transition(index, 0))
                next_transitions.append(Transition(index, 1))
                next_answers.append(TempAnswer(answer.copy(), next_transitions.copy()))

                next_transitions = next_transitions[:-3]
                amswer = answer[:-1]

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
    print(solution.nQueen(5))
