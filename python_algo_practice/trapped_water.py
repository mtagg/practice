




def trap(self, height):
  """
  :type height: List[int]
  :rtype: int
  """
  left, right = 0, len(height) - 1
  left_max, right_max, trapped = 0, 0, 0
  
  while left <= right:
      if left_max <= right_max:
          trapped += max(0, (left_max - height[left]))
          left_max = max(left_max, height[left])
          left += 1
      elif right_max < left_max:
          trapped += max(0, (right_max - height[right]))
          right_max = max(right_max, height[right])
          right -= 1
  
  
  return trapped
        


def main():
  levels = [1,0,1,0,1,2,3,0,1,2,1,3,1,0]
  print(trap(levels))

 
main()