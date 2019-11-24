#!/usr/bin/env python3

import argparse
import os
import sys
import csv

def returnIndex(array, string):
    index = ""
    print(string in array[0])
    for item in array:
        if string in item:
            index = item.index(string)
    return index

def testMissField(index, f, inputName):
    if (index == ""):
        errorMessage = "Error: " + inputName + ": no field with name closer found"
        f.write(errorMessage)
        exit()

def testGroupBy(index, f, inputName, groupByName):
    if (index == ""):
        errorMessage = "Error: " + inputName + ": no group-by arguement with name " + groupByName
        f.write(errorMessage)
        exit()

def testFileExist(f, inputName):
    if (not(os.path.exists(inputName))):
        errorMessage = "Error: " + inputName + ": no file exist"
        f.write(errorMessage)
        exit()

def findcount(array, index):
    total = 0
    for item in array:
        total = total + 1
    return total

def findmax(array, index):
    tempArray = []
    for item in array:
        tempArray.append(item[index])
    return max(tempArray)

def findmin(array, index):
    tempArray = []
    for item in array:
        tempArray.append(item[index])
    return min(tempArray)

def findmean(array, index):
    sumNum = 0
    ave = 0
    count = 0
    for row in array:
        sumNum = sumNum + float(row[index])
        count += 1
    ave = float(sumNum / count)
    return ave

def findsum(array, index):
    sumNum = 0
    for row in array:
        sumNum = sumNum + float(row[index])
    return sumNum


def main():
    # deliberately left blank for your implementation - remove this comment and begin
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="count total", action="store_true")
    parser.add_argument("--max", help="get max")
    parser.add_argument("--top", help="get the top num of item", action="append", nargs=2)
    parser.add_argument("--min", help="get min")
    parser.add_argument("--mean", help="get average")
    parser.add_argument("--sum", help="get sum")
    parser.add_argument("--input", help="get input")
    parser.add_argument("--group-by", help="if group by", dest="grp")
    
    
    
    fw = open("output.csv", "w")
    args = parser.parse_args()
    if (args.input):
        testFileExist(fw,args.input)
        with open(args.input) as fr:
            reader = csv.reader(fr)
            storeList = []
            forTopKListName = []#!!
            for item in reader:
                storeList.append(item)
            if (args.grp):
                fileHeader = [args.grp]
                tempHeader = fileHeader[:]
                listName =[]
                index = returnIndex(storeList, args.grp)
                print(index)#try to test with --group-by Sector and Ticker
                testGroupBy(index, fw, args.input, args.grp)
                for item in storeList:
                    if (item == storeList[0]):
                        continue
                    if (not(item[index] in listName)):
                        listName.append(item[index])
                forTopKListName = listName[:]#!!
                newList = []
                finalResult = []
                for i in range (len(listName)):
                    for row in storeList:
                        if (row == storeList[0]):
                            continue
                        if listName[i] == row[index]:
                            newList.append(row)
                    resultList = []
                    forTopKList = []#!!
                    resultList.append(listName[i])
                    if (args.count):
                        tempHeader.append("count")
                        total = findcount(newList, args.count)
                        resultList.append(total)
                    if (args.max):
                        newAppend = "max_" + args.max
                        tempHeader.append(newAppend)
                        indext = returnIndex(storeList, args.max)
                        testMissField(indext, fw, args.input)
                        max = findmax(newList, indext)
                        resultList.append(max)
                    if (args.min):
                        newAppend = "min_" + args.min
                        tempHeader.append(newAppend)
                        indext = returnIndex(storeList, args.min)
                        testMissField(indext, fw, args.input)
                        min = findmin(newList, indext)
                        resultList.append(min)
                    if (args.mean):
                        newAppend = "mean_" + args.mean
                        tempHeader.append(newAppend)
                        indext = returnIndex(storeList, args.mean)
                        testMissField(indext, fw, args.input)
                        mean = findmean(newList, indext)
                        resultList.append(mean)
                    if (args.sum):
                        newAppend = "sum_" + args.sum
                        tempHeader.append(newAppend)
                        indext = returnIndex(storeList, args.sum)
                        testMissField(indext, fw, args.input)
                        sum = findsum(newList, indext)
                        resultList.append(sum)
                    if (args.top):
                        newAppend = "top_" + args.top[0][1]
                        tempHeader.append(newAppend)
                        total = findcount(newList, args.count)
                        topK = ""
                        for j in range (len(listName)):
                            forTopKTemp = listName[j] + ": " + str(total)
                            forTopKList.append(forTopKTemp)
                        for j in range (len(args.top[0][0])):
                            topK += forTopKList[j]
                        resultList.append(topK)
                    finalResult.append(resultList)
                    newList = []
                    if (i == 0):
                        fileHeader = tempHeader[:]
                    resultList = []
                writer = csv.writer(fw)
                writer.writerow(fileHeader)
                writer.writerows(finalResult)
            else:
                fileHeader = []
                finalResult = []
                tempList = storeList[1:]
                if (args.count):
                    total = findcount(tempList, indext)
                    fileHeader.append("count")
                    finalResult.append(total)
                if (args.max):#have no idea why its always smaller than it should be
                    newAppend = "max_" + args.max
                    indext = returnIndex(storeList, args.max)
                    testMissField(indext, fw, args.input)
                    max = findmax(tempList, indext)
                    fileHeader.append(newAppend)
                    finalResult.append(max)
                if (args.min):
                    newAppend = "min_" + args.min
                    indext = returnIndex(storeList, args.min)
                    testMissField(indext, fw, args.input)
                    min = findmin(tempList, indext)
                    fileHeader.append(newAppend)
                    finalResult.append(min)
                if (args.mean):
                    newAppend = "mean_" + args.mean
                    indext = returnIndex(storeList, args.mean)
                    testMissField(indext, fw, args.input)
                    mean = findmean(tempList, indext)
                    fileHeader.append(newAppend)
                    finalResult.append(mean)
                if (args.sum):
                    newAppend = "sum_" + args.sum
                    indext = returnIndex(storeList, args.sum)
                    testMissField(indext, fw, args.input)
                    sum = findsum(tempList, indext)
                    fileHeader.append(newAppend)
                    finalResult.append(sum)
                if (args.top):
                    newAppend = "top_" + args.top[0][1]
                    fileHeader.append(newAppend)
                    index = returnIndex(storeList, args.top[0][1])
                    listName = []
                    forTopKList = []
                    forTopKListTemp = []
                    newList = []
                    for item in storeList:
                        if (item == storeList[0]):
                            continue
                        if (not(item[index] in listName)):
                            listName.append(item[index])
                    for i in range (len(listName)):
                        for row in storeList:
                            if (row == storeList[0]):
                                continue
                            if listName[i] == row[index]:
                                newList.append(row)
                        total = findcount(newList, args.count)
                        forTopKListTemp.append(total)
                        newList = []
                    topK = ""
                    for j in range (len(listName)):
                        forTopKTemp = listName[j] + ": " + str(forTopKListTemp[j]) + ","
                        forTopKList.append(forTopKTemp)
                    for j in range (int(args.top[0][0])):
                        topK += forTopKList[j]
                    finalResult.append(topK)

                writer = csv.writer(fw)
                writer.writerow(fileHeader)
                writer.writerow(finalResult)

if __name__ == '__main__':
    main()
