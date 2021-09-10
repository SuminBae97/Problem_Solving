def solution(n, lost, reserve):
    reser_del = set(reserve) - set(lost)
    lost_del = set(lost) - set(reserve)


    for i in reser_del:
        if i-1 in lost_del:
            lost_del.remove(i-1)
        elif i+1 in lost_del:
            lost_del.remove(i+1)

    return n-lost_del




    # num_of_ware = [1 for _ in range(n)]
    #
    # for val in lost:
    #     num_of_ware[val - 1] = 0
    #
    # for val in reserve:
    #     num_of_ware[val - 1] = num_of_ware[val - 1] + 1
    #
    # for i in range(len(num_of_ware)):
    #     try:
    #         # if num_of_ware[i] == 0 and (num_of_ware[i + 1] == 2 or num_of_ware[i-1]==2):
    #         #     num_of_ware[i] += 1
    #         #     num_of_ware[i + 1] -= 1
    #
    #         if num_of_ware[i]==0:
    #             val_left = num_of_ware[i-1]
    #             val_right = num_of_ware[i+1]
    #
    #             if val_left==2:
    #                 num_of_ware[i]+=1
    #                 num_of_ware[i-1]-=1
    #             elif val_right==2:
    #                 num_of_ware[i]+=1
    #                 num_of_ware[i+1]-=1
    #             else:
    #                 pass
    #
    #     except IndexError:
    #         pass
    #
    # count = 0
    # for val in num_of_ware:
    #     if val!=0:
    #         count+=1
    # print(num_of_ware)
    # print(count)
    # return count


solution(4,[3,1,2],[2,4,3])








