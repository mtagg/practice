'''
Solutions:
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVlfX1hPaHRZZW84endGM3dZRDZtSngtVVluUXxBQ3Jtc0ttNHdpTzJMTDMwZ1g1Yko2NlNIem1lUmtNUnE4eGgtU052VjE0WXB0QkdxeTZhNGxYWnZJVzROR21BbWlLXzlnbXREaXhtUWpiTm05SThxQ3ZrMnFhc3pXbV9Wanc1U05FQllKcUQwZXJ1ZVhCNVRxbw&q=https%3A%2F%2Fgist.github.com%2Fsyphh%2F173172ec9a4a1376e5096a187ecbddc9&v=Peq4GCPNC5c
YouTube Video:
https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2224s&ab_channel=freeCodeCamp.org
'''


# Takes an already sorted array, and returns the first and last instance index of a 
# particular number denoted by input cariable, n


      
def findFirst(arr,n,first,mid,last):
  if arr[mid] > n:
    l = mid
    m = int((l-first)/2) + first
    return findFirst(arr, n, first, m, l)
  elif arr[mid] < n:
    f = mid
    m = int((last-f)/2) + f
    return findFirst(arr, n, f, m, last)
  elif arr[mid] == n:
    if arr[mid-1] < n or arr[mid]==arr[first]:
      return mid
    else:
      l = mid
      m = int((l-first)/2) + first
      return findFirst(arr, n, first, m, l)

def findLast(arr,n,first,mid,last):
  if arr[mid] > n:
    l = mid
    m = int((l-first)/2) + first
    return findLast(arr, n, first, m, l)
  elif arr[mid] < n:
    f = mid
    m = int((last-f)/2) + f
    return findLast(arr, n, f, m, last)
  elif arr[mid] == n:
    if arr[mid+1] > n or arr[mid]==arr[last]:
      return mid
    else:
      f = mid
      m = int((last-f)/2) + f
      return findLast(arr, n, f, m, last)
    
  


def firstLastIndexOf(arr, n):
  arr = sorted(arr)
  first = 0
  last = len(arr) - 1

  mid = int((last-first)/2)
  return findFirst(arr,n,first,mid,last), findLast(arr,n,first,mid,last)
  






def main():
  arr = [1,2,2,2,4,5,5,5,6,6,6,7,7,8,9,9,9,0,5,5,5]
  n = 2
  first, last = firstLastIndexOf(arr, n) #should be index 8 and 10
  print("First index of " + str(n) + " is " + str(first))
  print("Last index of " + str(n) + " is " + str(last))
  
  
main()
