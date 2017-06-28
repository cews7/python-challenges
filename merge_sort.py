def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        left = merge_sort(array[:int(len(array)/2)])
        right = merge_sort(array[int(len(array)/2):])
        return merge_bi_dir(left, right)


def merge_bi_dir(left, right):
    if left[0] > right[0]:
        
