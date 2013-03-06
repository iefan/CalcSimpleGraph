#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#from string import zfill as z

def nscale(n=5, m=3):
    '''本程序可以寻找 n 阶 m 边的所有非同构简单图，并将其各点的度数打印出来。

    本程序实现思路：
        先将所有的度数序列用 n-1 进制表示出来，其个数的计算即：
        最大一个值是(maxEdgeNumber, maxEdgeNumber, maxEdgeNumber, ..., maxEdgeNumber), 其个数其有n个
        所以如果以maxEdgeNumber+1进制进行表示，即总个数有pow(maxEdgeNumber+1, n)个。

        而后对各序列进行求和，其和等于简单图总度数的，就是可能满足的序列。
        之后再对这些剩存的序列进行判断，满足条件的即为所求简单图。

        判断简单图的方法：
        (1) 将度数序列从大到小排序，如(n1,n2,...,nn)
        (2) 取掉n1, 将余下的其余n-1个数中的前n1个减1，再按从大到小排序
        重复(1)(2)步骤，直到余下的序列中若有-1，则不是简单图，若全零，即为简单图。

    maxEdgeNumber         : 该简单图中各顶点所具有的最大度数，也即从各顶点出来的最多边数
    totaldegree           : 该简单图中所有顶点的度数之和，也即边数的2倍
    allNumList            : 产生所有可能满足简单图条件的度数序列组合
    SimpleGraphDegreeList : 将 allNumList 中各度数序列进行检测后，符合简单图条件的序列之组合
    '''
    maxEdgeNumber = min(n-1, m)
    totaldegree = 2*m
    allNumList = [] # all seriers, they need be judge
    for inum in range(1, pow(maxEdgeNumber+1, n)):
        tmpbase = CalNumBase(inum, n, [])
        tmpbase.sort(reverse = True)
        #tmpbase = tuple(tmpbase)
        if sum(tmpbase) == totaldegree and (tmpbase not in allNumList):
            allNumList.append(tmpbase)

    SimpleGraphDegreeList = []
    for ilst in allNumList:
        if JudgeDegreeList(tuple(ilst)): # 之所以采用tuple传递，是因为防止ilst被程序更改掉
            SimpleGraphDegreeList.append(ilst)

    print SimpleGraphDegreeList

def CalNumBase(num=140, n=5, lstnum=[]):
    '''计算 n 进制数，并用列表返回'''
    if num<n:
        lstnum.insert(0, num)
        lenlst = len(lstnum)
        [lstnum.insert(0, 0) for i in range(lenlst, n)]
        return lstnum
    else:
        re = num%n
        lstnum.insert(0, re)
        num = num/n
        return CalNumBase(num, n, lstnum)

def JudgeDegreeList(lstdegree = [2,1,1,1,1]):
    lstdegree = list(lstdegree)
    lstdegree.sort(reverse = True)
    if -1 in lstdegree:
        return False
    elif lstdegree.count(0) == len(lstdegree):
        return True
    else:
        for indx in range(0, lstdegree.pop(0)):
            lstdegree[indx] = lstdegree[indx]-1
        return JudgeDegreeList(lstdegree)

def CalNumBase2(num=140, n=5, strnum = ""):
    if num<n:
        strnum = str(num) +strnum
        return z(strnum, n)
    else:
        re = num%n
        strnum = str(re) + strnum
        num = num/n
        return z(CalNumBase2(num, n, strnum), n)

if __name__ == '__main__':
#    JudgeDegreeList()
    nscale(5,7)
#    print CalNumBase()
