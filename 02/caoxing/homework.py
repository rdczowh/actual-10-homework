#!/usr/bin/env python
#coding=utf8
#arr=[1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,5000]
arr=[111111111111111111111111111111111111111111,66666666666666666666666,5555555160000,5000,1,2,3,2,12,3,1,3,21,2,2,3,4111,22,3333,444,111,4,5,777,65555,45,33,45,222222,4444444444,333333]
#arr=[1,2,3,4,2,12,3,14,3,2,12,3,14,3,21,2,2,3,4111,22,3333,4]
print "排序前:%s"%(arr)
length=len(arr)

for i in range(length - 1):
    if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
        for j in range(i):
            if arr[i] < arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
print "排序后:%s"%(arr)
