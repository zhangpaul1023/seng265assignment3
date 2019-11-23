#!/usr/bin/env python3

import argparse
import os
import sys
import csv

def returnIndex(Reader, string):
    index = 0
    for row in Reader:
        if string in row:
            index = row.index(string)
    return index

def findcount(array, index):
    total = 0
    for i in range (len(array)):
	total++
    return total

def findmax(array, index):
    maxNum = 0
    tempArray = []
    for i in range (len(array)):
        tempArray.append(array[i][index])
    return max(tempArray)

def findmin(reader, string):
    minNum = 99999999999999999999999999999999
    tempArray = []
    for i in range (len(array)):
	tempArray.append(array[i][index])
    return min(tempArray)

def findmean(dictReader, string):
    sumNum = 0
    ave = 0
    count = 0
    for row in dictReader:
	tempNum = int(row[string])
	sumNum += tempNum
	count += 1
    ave = int(sumNum / count)
    return ave

def findsum(dictReader, string):
    sumNum = 0
    for row in dictReader:
	temp = int(row[string])
	sumNum += temp
    return sumNum


def main():
    # deliberately left blank for your implementation - remove this comment and begin
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="count total")
    parser.add_argument("--max", help="get max")
    parser.add_argument("--min", help="get min")
    parser.add_argument("--mean", help="get average")
    parser.add_argument("--sum", help="get sum")
    parser.add_argument("--input", help="get input")
    parser.add_argument("--group-by", help="if group by", dest="grp")
    
    
    
    
    fw = open("output.csv", "w")
    args = parser.parse_args()
    if (args.input):
	fr = open(args.input, "r")
	reader = csv.reader(fr)
	if (args.grp):
	    fileHeader = [args.grp+","]
	    print(fileHeader)
	    resultList = []
	    listName =[]
	    result = {}
	    index = returnIndex(reader, args.grp)
	    for item in reader:
        	if reader.line_num == 1:
		    continue
        	if item[index] not in (listName):
		    listName.append(item[0][index])
	    print(listName)
	    newList = []
	    for i in range (len(listName)):
		print(1)
		for row in reader:
		    if reader.line_num == 1:
			continue
		    elif listName[i] in row:
			newList.append(row)
		if (args.count):
		    fileHeader.append(args.count)
		    total = findcount(newList, args.count)
		    resultList.append(total)
		if (args.max):
		    newAppend = "max_" + args.max
		    fileHeader.append(newAppend)
		    index = returnIndex(reader, args.max)
		    max = findmax(newList, index)
		    resultList.append(max)
	    	if (args.min):
		    newAppend = "min_" + args.min
		    fileHeader.append(newAppend)
		    min = findmin(newList, args.min)
		    resultList[newAppend] = min
	    	if (args.mean):
		    newAppend = "mean_" + args.mean
		    fileHeader.append(newAppend)
		    mean = findmean(newList, args.mean)
		    resultList[newAppend] = mean
	    	if (args.sum):
		    newAppend = "sum_" + args.sum
		    fileHeader.append(newAppend)
		    sum = findsum(newList, args.sum)
		    resultList[newAppend] = sum
		writer = csv.writer(fw)
		writer.writerow(fileHeader)
		write.writerow(resultDict)
		print(fileHeader)
		print(resultList)
		newList = {}
		resultList = {}

	else:
	    if (args.count):
                total = str(findcount(reader, args.count))
                fw.write("count,\n")
		fw.write(count+",")
            if (args.max):
                max = str(findmax(reader, args.max))
                fw.write("max_"+ args.max +",\n")
                fw.write(max+",")
            if (args.min):
                min = str(findmin(reader, args.min))
                fw.write("min_"+ args.min +",\n")
                fw.write(min+",")
            if (args.mean):
                mean = str(findmean(reader, args.mean))
                fw.write("mean_"+ args.mean +",\n")
                fw.write(mean+",")
            if (args.sum):
                sum = str(findsum(reader, args.sum))
                fw.write("sum_"+ args.sum +",\n")
                fw.write(sum+",")


if __name__ == '__main__':
    main()
