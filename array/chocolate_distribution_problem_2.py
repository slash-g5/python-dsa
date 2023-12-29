# problem link https://www.geeksforgeeks.org/chocolate-distribution-problem-set-2/

def solve(students_score):
    ans_array = []
    num_students = len(students_score)
    if num_students == 0:
        return ans_array
    ans_array.append(1)
    curr_index = 1
    while curr_index < num_students:
        if students_score[curr_index] >= students_score[curr_index - 1]:
            ans_array.append(ans_array[curr_index - 1] + 1)
        elif students_score[curr_index] < students_score[curr_index - 1]:
            ans_array.append(1)
            temp_index = curr_index
            while ans_array[temp_index] == ans_array[temp_index - 1]:
                ans_array[temp_index - 1] = ans_array[temp_index - 1] + 1
                temp_index -= 1
                if temp_index == 0:
                    break
        curr_index += 1

    return ans_array


if __name__ == '__main__':
    print(solve([2, 8, 1, 87, 56, 32, 45, 765, 7, 4, 9, 6, 87, 34]))
