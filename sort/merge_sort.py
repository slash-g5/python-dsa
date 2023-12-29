a1 = [1, 4, 1, 3, 76, 10, 56, 4325, 21312, 234, 1, 2, 1, 2, 0, 0, 0]


def merge_sort(array):
    def merge_sort_helper(split_array, start, end):
        if end <= start:
            return
        if end == start + 1:
            if split_array[start] > split_array[start + 1]:
                temp = split_array[start]
                split_array[start] = split_array[start + 1]
                split_array[start + 1] = temp
            return
        mid = start + (end - start + 1) // 2
        merge_sort_helper(split_array, start, mid)
        merge_sort_helper(split_array, mid + 1, end)
        i = start
        j = mid+1
        merge_array = []
        while i <= mid or j <= end:
            if i <= mid and j <= end:
                if split_array[i] <= split_array[j]:
                    merge_array.append(split_array[i])
                    i += 1
                else:
                    merge_array.append(split_array[j])
                    j += 1
                continue
            if i <= mid:
                merge_array.append(split_array[i])
                i += 1
                continue
            if j <= end:
                merge_array.append(split_array[j])
                j += 1
        for i in range(start, end+1):
            split_array[i] = merge_array[i-start]
        return
    merge_sort_helper(array, 0, len(array) - 1)


if __name__ == "__main__":
    print(a1)
    merge_sort(a1)
    print(a1)
