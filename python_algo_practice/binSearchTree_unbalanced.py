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
 
  def __init__(self, val):
    self.parentNode = Node(val) 
  
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
  

def printTreeValues(node):
  if node == None:
    return
  else:
    printTreeValues(node.left)
    print(node.value)
    printTreeValues(node.right)

def main():
  tree = BinTree(5)
  tree.addNode(tree.parentNode,1)
  tree.addNode(tree.parentNode,6)
  tree.addNode(tree.parentNode,2)
  tree.addNode(tree.parentNode,3)
  tree.addNode(tree.parentNode,4)
  tree.addNode(tree.parentNode,5)
  printTreeValues(tree.parentNode)


main()