# User function Template for python3
# https://www.geeksforgeeks.org/problems/activity-selection-1587115620/1

class Solution:

    # Function to find the maximum number of activities that can
    # be performed by a single person.
    def activitySelection(self, n, start, end):

        # code here
        start_end = [(start[i], end[i]) for i in range(len(start))]
        start_end.sort(key=lambda x: x[1])

        count = 0
        prev_end = -1

        for i in range(len(start_end)):
            if start_end[i][0] > prev_end:
                count += 1
                prev_end = start_end[i][1]

        return count