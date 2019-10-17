# Prints sums of all subsets of arr[l..r] 
def subsetSums(arr, l, r, sum = 0): 
    # print(str(sum) + "/"*40 + str(l) + "-" + str(r))       
    # Print current subset 
    if l > r: 
        print(sum, end = " ") 
        return
  
    # Subset including arr[l] 
    subsetSums(arr, l + 1, r, sum + arr[l])
  
    # Subset excluding arr[l] 
    subsetSums(arr, l + 1, r, sum)  
  
# Driver code 
arr = [5, 4, 3] 
n = len(arr) 
subsetSums(arr, 0, n - 1) 


# Python 3 recursive program to print  
# all n-digit numbers whose sum of  
# digits equals to given sum 
  
# Recursive function to print all  
# n-digit numbers whose sum of  
# digits equals to given sum 
  
# n, sum --> value of inputs 
# out --> output array 
# index --> index of next digit to be  
#            filled in output array 
def findNDigitNumsUtil(n, sum, out,index): 
  
    # Base case 
    if (index > n or sum < 0): 
        return
  
    f = "" 
      
    # If number becomes N-digit 
    if (index == n): 
      
        # if sum of its digits is equal 
        # to given sum, print it 
        if(sum == 0): 
            out[index] = "" 
              
            for i in out: 
                f = f + i 
            print(f, end = " ") 
          
        return
  
    # Traverse through every digit. Note  
    # that here we're considering leading 
    # 0's as digits 
    for i in range(10): 
          
        # append current digit to number 
        out[index] = chr(i + ord('0')) 
  
        # recurse for next digit with reduced sum 
        findNDigitNumsUtil(n, sum - i,  
                           out, index + 1) 
  
# This is mainly a wrapper over findNDigitNumsUtil. 
# It explicitly handles leading digit 
def findNDigitNums( n, sum): 
  
    # output array to store N-digit numbers 
    out = [False] * (n + 1) 
  
    # fill 1st position by every digit  
    # from 1 to 9 and calls findNDigitNumsUtil()  
    # for remaining positions 
    for i in range(1, 10): 
        out[0] = chr(i + ord('0')) 
        print(out)
        findNDigitNumsUtil(n, sum - i, out, 1) 
  
# Driver Code 
n = 2
sum = 3

findNDigitNums(n, sum) 
  
grades = ['A', 'B', 'C', 'D', 'E', 'F']

for i, grade in enumerate(grades, 1):
    print(f'{i} : {grade}')

cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'e', 'J', 'Q', 'K' )

# extract ace, 2, 3 only
ace, two, three, *_ = cards
print(ace, two, three)
ace, *numbers, J, Q, K = cards
print(ace, numbers, J, Q, K)
lst1 = [3, 1, 2, 4, 7, 5, 6, 9, 8]
def quicksort(lst):
    "Quicksort over a list-like sequence"
    if len(lst) == 0:
        return lst
    pivot = lst[0]
    pivots = [x for x in lst if x == pivot]
    small = quicksort([x for x in lst if x < pivot])
    large = quicksort([x for x in lst if x > pivot])
    return small + pivots + large
print(quicksort(lst1))

def subs(l):
    if l == []:
        return [[]]

    x = subs(l[1:])
    for i in x + [[l[0]] + y for y in x]:
        print("*"*40)
        print(i)
        print("?"*40)

    return x + [[l[0]] + y for y in x]
print(subs(lst1))
print(lst1)
