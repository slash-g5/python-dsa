class Solution:
    # count total number of atoms in a formula
    # for eg:
    # formula ="K4(ON(SO3)2)2"
    # Output= 24
    def countOfAtoms(self, formula: str) -> str:
        answer = 0
        i = 0
        stack = []
        while i < len(formula):
            if ord('a') <= ord(formula[i]) <= ord('z'):
                i += 1
                continue
            if ord('A') <= ord(formula[i]) <= ord('Z'):
                answer += 1
                i += 1
                continue
            if ord('0') <= ord(formula[i]) <= ord('9'):
                answer += int(formula[i]) - 1
                i += 1
                continue
            if formula[i] == '(':
                stack.append(answer)
                i += 1
                continue
            if formula[i] == ')':
                if i == len(formula) - 1:
                    return answer
                if ord('0') > ord(formula[i + 1]) or ord('9') < ord(formula[i + 1]):
                    stack.pop()
                    i += 1
                    continue
                if not stack:
                    return -1

                i += 1
                prev = stack.pop()
                curr_count = answer - prev
                b_count = 0
                while i < len(formula) and ord('0') <= ord(formula[i]) <= ord('9'):
                    b_count = b_count * 10 + int(formula[i])
                    i += 1
                b_count -= 1
                answer += curr_count * b_count

        return answer