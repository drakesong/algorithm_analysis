# CS 317 Algorithm Anaylsis Lab 3
# Drake Song
# Python 3.6
# All of the following sorting algorithms have been copied from CodeCodex with
# some adjustments to make sure the program runs smoothly as a whole.

import numpy as np
import timeit
import csv

def bubblesort(input_list):
    lst = input_list[:]
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(lst)-1):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
    return lst

def insertsort(input_list):
    lst = input_list[:]
    for removed_index in range(1, len(lst)):
        removed_value = lst[removed_index]
        insert_index = removed_index
        while insert_index > 0 and lst[insert_index - 1] > removed_value:
            lst[insert_index] = lst[insert_index - 1]
            insert_index -= 1
        lst[insert_index] = removed_value
    return lst

def selectionsort(input_list):
    lst = input_list[:]
    l=lst[:]
    srt_lst=[]
    while len(l):
        lowest=l[0]
        for x in l:
            if x<lowest:
                lowest=x
        srt_lst.append(lowest)
        l.remove(lowest)
    return srt_lst

def mergesort(input_list):
    lst = input_list[:]
    if len(lst) == 1:
        return lst

    m = round(len(lst) / 2)
    l = mergesort(lst[:m])
    r = mergesort(lst[m:])

    if not len(l) or not len(r):
        return l or r

    result = []
    i = j = 0
    while (len(result) < len(r)+len(l)):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
        if i == len(l) or j == len(r):
            result.extend(l[i:] or r[j:])
            break

    return result

def quicksort(input_list):
    lst = input_list[:]
    if len(lst)<=1:
        return lst
    pivot=lst[0]
    less=    [x for x in lst if x<pivot]
    equal=   [x for x in lst if x==pivot]
    greater= [x for x in lst if x>pivot]
    lst = quicksort(less)+equal+quicksort(greater)
    return lst


def shellsort(input_list):
    lst = input_list[:]
    inc = int(round(len(lst) / 2))
    while inc:
        for i in range(len(lst)):
            j = i
            temp = lst[i]
            while j >= inc and lst[j-inc] > temp:
                lst[j] = lst[j-inc]
                j -= inc
            lst[j] = temp
        inc = int(inc/2) if inc/2 else (0 if inc==1 else 1)
    return lst




time_bub = []
time_ins = []
time_sel = []
time_mer = []
time_she = []
time_qui = []
time_sor = []
n = [1, 5, 10, 50, 100, 500, 1000, 2500, 5000, 10000]

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for j in n:
        print("starting n = {}".format(j))
        for i in range(25):
            x = np.random.randint(-1000000, 1000000, size=(j*10)).tolist()

            tic = timeit.default_timer()
            bubblesort(x)
            toc = timeit.default_timer()
            time_bub.append((toc-tic)*1000000)
            print("bubblesort is done")

            tic = timeit.default_timer()
            insertsort(x)
            toc = timeit.default_timer()
            time_ins.append((toc-tic)*1000000)
            print("insertsort is done")

            tic = timeit.default_timer()
            selectionsort(x)
            toc = timeit.default_timer()
            time_sel.append((toc-tic)*1000000)
            print("selectionsort is done")

            tic = timeit.default_timer()
            mergesort(x)
            toc = timeit.default_timer()
            time_mer.append((toc-tic)*1000000)
            print("mergesort is done")

            tic = timeit.default_timer()
            shellsort(x)
            toc = timeit.default_timer()
            time_she.append((toc-tic)*1000000)
            print("shellsort is done")

            tic = timeit.default_timer()
            quicksort(x)
            toc = timeit.default_timer()
            time_qui.append((toc-tic)*1000000)
            print("quicksort is done")

            tic = timeit.default_timer()
            sorted(x)
            toc = timeit.default_timer()
            time_sor.append((toc-tic)*1000000)
            print("sorted is done")


        bub = sum(time_bub)/25
        ins = sum(time_ins)/25
        sel = sum(time_sel)/25
        mer = sum(time_mer)/25
        she = sum(time_she)/25
        qui = sum(time_qui)/25
        sor = sum(time_sor)/25

        writer.writerow((j, bub, ins, sel, mer, she, qui, sor))
        print("{} is done\n".format(j))
