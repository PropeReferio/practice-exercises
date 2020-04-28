def create_array(size=10, maxval=50):
    import random
    return [random.randint(0, maxval+1) for i in range(size)]

arr = create_array()
print(arr)

def bubble_sort(lst):
    for i in range(0, len(lst) - 1):
        for j in range(0, len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    return lst

print(bubble_sort(arr))

def merge(a,b):
    c = [] #Final return value
    a_idx, b_idx = 0, 0
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c


def merge_sort(a):
    # a list of 0 or 1 elements is already sorted.
    if len(a) <= 1: return a
    # recursively call merge_sort on the left and right halves of a until
    # the whole thing has been broken down into single element lists,
    #which can be merged by the merge function
    left, right = merge_sort(a[:len(a)//2]), merge_sort(a[len(a)//2:])
    #Merge with merge function
    return merge(left, right)


s = merge_sort(arr)
# print(s)