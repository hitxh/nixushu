while True:
    try:
        N = int(input().rstrip())
        num_list = input().rstrip().split()
        num_arr = [int(v) for v in num_list]
        nixushu = 0
        for i in range(N-1):
            sum([1 for v in num_arr[i::] if num_arr[i]>v])
            for v in num_arr[i+1::]:
                if num_arr[i]>v:
                    nixushu += 1
        print(nixushu)
        #break
    except:
        break