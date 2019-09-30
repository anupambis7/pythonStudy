# Insertion Sort
#Ref : https://www.youtube.com/watch?v=QnjToZfpi0E&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf&index=17

# We assume that the Seq is sorted till  sliceEnd -1 . So we come to sliceEnd and check if its smaller than than the previous value.
# We c

def InsertSort(InpSeq):
    for sliceEnd in range(len(InpSeq)):
        pos = sliceEnd
        while pos > 0 and InpSeq[pos] < InpSeq[pos -1]:
            (InpSeq[pos],InpSeq[pos -1]) = (InpSeq[pos-1],InpSeq[pos])
            pos = pos -1

seq1 = [1,2,3]
seq2 = [5,3,10,4]
# Itr 1 : [5,3,10,4]
# Itr 2 : [3,5,10,4]
# Itr 3 : [3,5,10,4] # Itr 4.1 : [3,5,4,10] # Itr 4.2 : [3,4,5,10]
# Itr 4 : [3,4,5,10]
print("Insertion Sort")
InsertSort(seq1)
print(seq1)
InsertSort(seq2)
print(seq2)

# Recusrsive Insertion Sort
#https://www.youtube.com/watch?v=TAOziHOk7iA&list=PL3pGy4HtqwD02GVgM96-V0sq4_DSinqvf&index=18


def InsertSortRecur(InpSeq,sliceEnd=0):
    pos = sliceEnd
    if pos != len(InpSeq):
        while pos > 0 and InpSeq[pos] < InpSeq[pos -1]:
            (InpSeq[pos] ,InpSeq[pos -1]) = (InpSeq[pos-1] ,InpSeq[pos])
            pos = pos-1
        return InsertSortRecur(InpSeq, sliceEnd+1)

seq1 = [1,2,3]
seq2 = [5,3,10,4]
print("Insertion Sort By Recursion")
InsertSortRecur(seq1)
print(seq1)
InsertSortRecur(seq2)
print(seq2)


# In Recusrsion Python imposes a limt on the recursion Limit. So if we go beyond this limit it throws an Error.We can change it though by below. There has be a max value set and this cannot be infinite.
import sys
sys.setrecursionlimit(1000) # setting this to 1000 in this case.


# Merge Sort

# Step 1 : Logic to Merging two sorted List
print("### Step 1 : Logic to Merging two sorted List ###")
def mergeSortedLst (Input_1,Input_2):
    (C,m,n) = ([],len(Input_1),len(Input_2))
    print("M+n" + str(m+n))
    (i,j) = (0,0)
    while j+i < m+n:
        print("value of i and is :" + str(i) +" " +str(j))
        if i == m:
            C.append(Input_2[j])
            j= j+1
        elif j == n:
            C.append(Input_1[i])
            i= i+1
        elif Input_1[i] <= Input_2[j]:
            C.append(Input_1[i])
            i = i + 1
        else :
            C.append(Input_2[j])
            j = j + 1
    return C

seq1 = [1,3,5]
seq2 = [2,4,10]

l = mergeSortedLst(seq1,seq2)
print(l)


def mergeSort (A,left,right):
    if right - left <=1 :
        return A[left:right]
    else :
        mid = (left + right) //2
        L = mergeSort(A,left,mid)
        R = mergeSort(A, mid, right)

        return mergeSortedLst(L,R)


def mergeSortMain(A):
    length = len(A)
    return mergeSort(A,0,length)

print("Calling main merge Sort")
seqMergeSort1= [4,1,6,7,2,0]
print(mergeSort(seqMergeSort1,0,len(seqMergeSort1)))
print(mergeSortMain(seqMergeSort1))
