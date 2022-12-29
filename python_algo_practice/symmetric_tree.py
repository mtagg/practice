'''
Solutions:
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVlfX1hPaHRZZW84endGM3dZRDZtSngtVVluUXxBQ3Jtc0ttNHdpTzJMTDMwZ1g1Yko2NlNIem1lUmtNUnE4eGgtU052VjE0WXB0QkdxeTZhNGxYWnZJVzROR21BbWlLXzlnbXREaXhtUWpiTm05SThxQ3ZrMnFhc3pXbV9Wanc1U05FQllKcUQwZXJ1ZVhCNVRxbw&q=https%3A%2F%2Fgist.github.com%2Fsyphh%2F173172ec9a4a1376e5096a187ecbddc9&v=Peq4GCPNC5c
YouTube Video:
https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2224s&ab_channel=freeCodeCamp.org
'''

class Node:
  value = None
  left = None
  right = None
  
  def __init__(self,val):
    self.value = int(val)
    
    
class BinTree:
  parentNode = None
  # leftDepth = None
  # rightDepth = None
 
  def __init__(self, val):
    self.parentNode = Node(val) 
    # leftDepth = 0
    # rightDepth = 0
  
  def addNode(self, node, val):
    if self.parentNode is None:
      self.parentNode = Node(val)
      return
    
    else:
      if node.value < val:
        if node.right is None:
          newNode = Node(val)
          node.right = newNode
        else:
          self.addNode(node.right, val)
      else: # node.value >= val
        if node.left is None:
          newNode = Node(val)
          node.left = newNode
        else:
          self.addNode(node.left, val)
    
def checkRightTree (node):
  if node == None:
    return " "
  else:
    return str(node.value) + checkRightTree(node.right) + checkLeftTree(node.left) 
    
def checkLeftTree (node):
  if node == None:
    return " "
  else:
    return str(node.value) + checkLeftTree(node.left) + checkRightTree(node.right) 
    
  
def isTreeSymmetric(tree):
  if (tree.parentNode == None):
    return True
  else:
    l = checkLeftTree(tree.parentNode.left)
    # print(l)
    r = checkRightTree(tree.parentNode.right)
    # print(r)
    return l == r

def printTreeValues(node):
  if node == None:
    return
  else:
    printTreeValues(node.left)
    print(node.value)
    printTreeValues(node.right)

def main():
  tree = BinTree(5)
  tree.parentNode.left = Node(1)
  tree.parentNode.right = Node(1)
  tree.parentNode.right.left = Node(5)
  tree.parentNode.left.right = Node(5)
  # tree.addNode(tree.parentNode,6)
  # tree.addNode(tree.parentNode,2)
  # tree.addNode(tree.parentNode,3)
  # tree.addNode(tree.parentNode,4)
  # tree.addNode(tree.parentNode,5)
  printTreeValues(tree.parentNode)
  print(isTreeSymmetric(tree))


main()