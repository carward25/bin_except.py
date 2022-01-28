#name: cassidy ward
#date: 1/26/2022
#description: modify the binary search from the exploration

#class excption - target not found
class TargetNotFound(Exception):
  pass

def binary_search(a_list, target):
   """Searches a_list for an occurrence of target. If found, returns the index of its position in the list. If not found, returns -1, indicating the target value isn't in the list """
   first = 0
   last = len(a_list) - 1
   while first <= last:
     middle = (first + last) // 2
     if a_list[middle] == target:
       return middle
       if a_list[middle] > target:
         last = middle - 1
         else:
         first = middle + 1
         raise TargetNotFound