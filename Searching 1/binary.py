print("This is Binary Search")
def binarySearchAppr (arr, start, end, x):
   if end >= start:
    #  mid = start + (end- start)//2
      mid = (start + end)//2
      if arr[mid] == x:
        return mid
      elif arr[mid] > x:
        return binarySearchAppr(arr, start, mid-1, x)#less than mid value
      else:
        return binarySearchAppr(arr, mid+1, end, x)#more than mid value
   else:
      return -1
arr = sorted(['i','m','a','t','r','e','e'])
print (arr)
x =input("Enter the element to search: ")
result = binarySearchAppr(arr, 0, len(arr)-1, x)
if result != -1:
  print ("Element is present at index "+str(result))
else:
   print ("Element is not present in array")