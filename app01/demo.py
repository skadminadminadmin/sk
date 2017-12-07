my_list = [8,1,2,4,6,3,7,5,9]

def select_sort(item):
    '''
    选择排序
    解释：将每一个和所有的进行比较，重的下沉



    '''
    #我的反序实现，无语了，刚好是反过来，擦
    for i1,v1 in enumerate(item):
        for i2,v2 in enumerate(item):
            print(item)
            if v1 > v2:
                item[i1],item[i2] = item[i2],item[i1]
    # return item[::-1]
    return item


# l = [1,2,8]
l = [54,226,93,17,77,31,44,55,20]
# print(select_sort(l))
# print(select_sort(my_list))






























def bubble_sort(item):
    '''冒泡排序'''
    for i in range(len(item)-1,0,-1):
        for j in range(i):
            if item[j] > item[j+1]:
                item[j],item[j+1]=item[j+1],item[j]
    # for i in range(len(item)-1):
    #     for j in range(i):
    #         if item[j] > item[j+1]:
    #             item[j],item[j+1]=item[j+1],item[j]
    return item
# print(bubble_sort(my_list))
# print(insert_sort(my_list))


def insert_sort(item):
    '''
    插入排序
    介绍：插入排序的精髓和排序纸牌一样，向前排，前面的都是有序的，然后一直排到最后
    '''
    for i in range(1,len(item)):
        # 注意这里是从第二个元素开始的
        # for j in range(i,0,-1):
            # 从后向前遍历，如果后面的小于前面的，就向前移位
            # if item[j] < item[j-1]:
            #     item[j],item[j-1] = item[j-1],item[j]
        j = i
        while j > 0:
            #while实现
            if item[j] < item[j-1]:
                item[j],item[j-1] = item[j-1],item[j]
            j -= 1
    return item


def merger(aList,bList):
    cList = []
    i = 0
    j = 0
    while len(aList) > i and len(bList) > j:
        if len(aList) > len(bList):
            pass

    # if len(aList) == 0 or len(bList) == 0:
    #     return aList + bList
    # elif len(aList) < len(bList):
    #     for i,v in enumerate(aList):
    #         if v <= bList[i]:
    #             cList.append(v)
    #         else:
    #             cList.append(bList[i])
    #     cList.extend(bList[len(aList)-1:])
    # else:
    #     for j,v1 in enumerate(bList):
    #         if v1 <= aList[j]:
    #             cList.append(v1)
    #         else:
    #             cList.append(aList[len(bList)-1])
    #     print(cList)
    return cList

# print(merger([4,5],[1,2,3]))
def GetResult(LA,LB):
    LC=[]
    i=0;j=0
    while len(LA)>i and len(LB)>j:#取A和B中的元素并以此进行比较
        if LA[i]<LB[j]:
            LC.append(LA[i])
            i+=1
        else:
            LC.append(LB[j])
            j+=1
    while len(LA)>i:#如果A中元素剩余就将A中的元素进行添加
        LC.append(LA[I])
        i+=1
    while len(LB)>j:#如果B中元素剩余就将B中的元素进行添加
        LC.append(LA[j])
        j+=1

