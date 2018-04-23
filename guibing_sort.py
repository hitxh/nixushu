'''
输入

5
4 5 1 3 2
输出

7

'''
global nixushu

def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = int(len(lists))//2
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)

def Merge(left, right):
    global nixushu
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
            nixushu += len(left) - l
    result += right[r:]
    result += left[l:]
    return result


while True:
    try:
        nixushu = 0
        N = int(input().rstrip())
        num_list = input().rstrip().split()
        num_list = [int(v) for v in num_list]
        print(N)
        print(num_list)
        MergeSort(num_list)
        print(nixushu)
    except:
        break