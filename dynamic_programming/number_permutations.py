# User function Template for python3
# https://www.geeksforgeeks.org/problems/permutations-of-a-given-string2041/1

class Solution:
    def find_permutation(self, S):
        # Code here
        n = len(S)
        S_arr = list(S)
        S_arr.sort()

        dp_arr = [[] for _ in range(n + 1)]

        dp_arr[n].append(S[n - 1])

        for i in range(n - 1, 0, -1):
            next_dp = dp_arr[i + 1]
            for elem in next_dp:
                curr_temp = []
                curr_temp.append(S[i - 1] + elem)
                for j in range(len(elem)):
                    curr = elem[: j + 1] + S[i - 1] + elem[j + 1:]
                    curr_temp.append(curr)
                dp_arr[i].extend(curr_temp)
        final_list = dp_arr[1]
        final_list.sort()
        ans = []
        curr = ''

        for fl in final_list:
            if curr == fl:
                continue
            curr = fl
            ans.append(curr)

        return ans
