import time
import random

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark

def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

def main():
	t0 = time.time()
	alist = range(1,1000,1)
	random.shuffle(alist)
	insertionSort(alist)
	print(alist)
	t1 = time.time()
	total_a = t1-t0

	print(total_a)

	t2 = time.time()
 	blist = range(1,1000,1)
 	random.shuffle(blist)
 	quickSort(blist)
 	print(blist)
 	t3 = time.time()
 	total_b = t3-t2

 	print(total_b)

	t4 = time.time()
	clist = range(1,1000,1)
	random.shuffle(clist)
	selectionSort(clist)
	print(clist)
	t5 = time.time()
	total_c = t5-t4

	print(total_c)


if __name__ == "__main__":
    main()