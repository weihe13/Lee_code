# 算法稳定性：相同键值（对比值）的元素，排序后不改变原来的相对位置
# range(起点，终点，步长)： 不取终点

"""排序算法汇总"""

"""Bubble Sort冒泡排序法，时间复杂度为O（n^2）,可优化为O（n），稳定"""
"""1.把前后两个元素进行比较 2.交换 3.用交换后的元素继续比较 4.每一轮都可以把最大元素放在最后 / 交换元素逐个对比后面元素"""

def BubbleSort(alist):
    # 从1~n
    n = len(alist)
    # 创造循环，j表示每一次确定一个元素可少对比一次，最后一次j=n-2
    for j in range(0, n-1):
        # count优化代码，如果其中有一次元素都没有交换，直接退出循环，排序成功
        count = 0
        for i in range(0, n-1-j):
            # 交换步骤,从小到大,如果比上一位更大交换，如果相等和更小则不交换
            # range(0,n-1),表示下标从0~n-2，共n-1次
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1
        if count == 0:
            # 在其中一个循环没有交换元素表示排序成功,O(n)复杂度
            return
    """
    循环也可替换成：
    for j in range(len(alist)-1, 0, -1):
        for i in range(0, j):
    """

"""Select Sort选择排序法，时间复杂度为O（n^2），不稳定"""
"""1.设定最小值索引 2.一个循环比较值大小 3.交换索引 4.循环结束后最小值和最前面的值交换 5.最小值一直排在前面 / 找到最小值放在最前面"""

def SelectSort(alist):
    n = len(alist)
    # 最后一轮的时候j应等于n-2，才有i=j+1
    for j in range(0, n-1):
        min_index = j
        # 交换操作，经过一轮循环把最小值的索引找到，退出循环后交换值
        for i in range(j+1, n):
            if alist[min_index] > alist[i]:
                min_index = i
        alist[j], alist[min_index] = alist[min_index], alist[j]


"""Insertion Sort 插入排序法，时间复杂度O（n^2），稳定"""
"""1.设定头元素为参考值 2.后面元素和参考值对比 3.放在参考值的前后适当位置 4.后面元素和前面序列继续对比放在适当的位置 / 后面元素插入前面序列适当位置"""

def InsertionSort(alist):
    n = len(alist)
    # 外层循环控制对比数的下标
    for j in range(0, n-1):
        # 内层循环操作，在前面有序序列插入
        for i in range(j+1, 0, -1):
            if alist[i-1] > alist[i]:
                alist[i-1], alist[i] = alist[i], alist[i-1]
            # 优化函数，如果没有交换则不需要在进行下面循环，已找到合适的位置
            else:
                break

"""Shell Sort 希尔排序算法，时间复杂度O（n^2），不稳定"""
"""1.设计步长gap 2.按gap的个数分成gap组序列（当做索引位移下标） 3.每组序列都按插入算法排序 4.整合成一个序列 5.重新设定gap / 当gap=1时就是插入算法"""

def ShellSort(alist):
    n = len(alist)
    # gap作为分组的步长
    gap = 5
    # 最外层循环控制gap的取值次数
    while gap > 0:
        # 固定gap下，循环次数，从 gap ~ n-1
        for j in range(0, n - gap):
            # 内层循环操作，步长下的插入算法
            for i in range(j + gap, 0, -gap):
                # 因为以gap步长，可能使i-gap为负值，所以加上一个判断
                if i - gap >= 0:
                    if alist[i - gap] > alist[i]:
                        alist[i - gap], alist[i] = alist[i], alist[i - gap]
                    else:
                        break
        # //为地板除，除法后取整数位 5//2=2，所以gap取 5,2,1
        gap = gap // 2

"""Quick Sort快速排序算法，时间复杂度O(n^2),最优时间复杂度O(nlog(n)),把n个元素/2直到分成1个元素的次数为log(n)，每一次循环为n次,不稳定"""
"""1.设置low和high两个游标指向第一个和最后一个元素 2.设置要排序元素为mid 3.要使low左边的值都比mid小，high右边的值都比mid大 
   4.先动high游标，和mid进行对比，比mid小就把值丢给low 5.换low继续动，直到low比mid大，把值丢给high 6.low=high时为mid下标位置
   6.mid定位后把列表分为两部分 7.分别进行定位（递归方法） / 采用双游标夹击mid，分别行动，拆分序列再夹击，找到固定索引
"""
def QuickSort(alist, first, last):

    # 递归终止条件，要放在最开头直接退出，当分解到仅有一个元素就可以停止递归（注意为None的状态，可能会出现low+1>last）,return终止递归
    # =条件为一个元素，>条件为None
    if first >= last:
        return

    # 游标赋值
    low_index = first
    high_index = last
    mid = alist[first]

    # 总控制，只要两个不相等就继续进行分别移动
    while low_index < high_index:
        # high游标先动,相等的情况下进行处理，全部归于右边
        while low_index < high_index and alist[high_index] >= mid:
            high_index -= 1
        alist[low_index] = alist[high_index]

        # 找到例外退出循环换low进行移动，并再次判别值，避免两个游标错过
        while low_index < high_index and alist[low_index] < mid:
            low_index += 1
        alist[high_index] = alist[low_index]
        # 换high进行移动

    # 当两个游标相等的时候,赋值定位元素
    alist[low_index] = mid

    # 运用递归算法进行下一步计算
    # 传入完整的list才能保证下标定位是完整的，所以不能用切片算法，切片算法产生的是新的list，下标重新排序
    # 需要传入起始下标和终点下标，保证下标和原来一样
    QuickSort(alist, first, low_index-1)
    QuickSort(alist, low_index+1, last)

"""Merge Sort归并排序算法，时间复杂度O(nlog(n))，稳定，速度快但是空间开销大（产生新的列表）"""
"""1.先把n个元素以n/2/2/2...为一组拆分成单个元素（递归，单个元素为退出条件） 2.设置left和right两个游标 3.接收返回的新列表
   4.两个游标分别在两个组，把单个元素两两对比排序合并成一组 5.把两个组以相同方式对比合并成一组 5.直到合并成一个有序序列"""
# 方法的原则就是调其中的一层进行编写，并写递归终止条件，有返回值就要接收返回值

def MergeSort(alist):

    n = len(alist)
    # 先进行拆分，退出递归条件为拆分为单个元素，并把单个元素返回
    if n == 1:
        return alist
    n = n//2

    # 对序列进行对半拆分，并对子序列继续进行拆分,切片[0:n]不取n
    # 接收拆分完的返回值（且是排序完成后的序列）,取得返回值后继续进行下面的步骤，挑一层进行编写
    left_list = MergeSort(alist[:n])
    right_list = MergeSort(alist[n:])

    # 两个组分别设置一个游标和结果存放
    left_index = 0
    right_index = 0
    result = []

    # 两个组进行比较排序，有一边的游标到尽头的时候退出
    while left_index < len(left_list) and right_index < len(right_list):
        # 比较大小，存入较小元素后游标+1
        if left_list[left_index] <= right_list[right_index]:
            result.append(left_list[left_index])
            left_index += 1
        else:
            result.append(right_list[right_index])
            right_index += 1
    # 退出循环后把剩下的元素加在列表的后面，切片[left:0]超出序列返回空列表
    # 用append加上切片会把整个list加进去，+则把元素重新加到末尾
    result += left_list[left_index:]
    result += right_list[right_index:]

    # 返回排序完后的序列
    # 最底层循环返回单个元素list，后面循环返回排序完成后的list
    return result


from timeit import Timer
if __name__ == "__main__":
    list1 = [99,88,77,66,55,44,33,22,11,0]
    print(list1)
    print(MergeSort(list1))

"""函数操作时间计时器
    timer1 = Timer("InsertionSort1()", "from __main__ import InsertionSort1")
    print("after:", timer1.timeit(1000))

    timer2 = Timer("InsertionSort2()", "from __main__ import InsertionSort2")
    print("before:", timer2.timeit(1000))
"""