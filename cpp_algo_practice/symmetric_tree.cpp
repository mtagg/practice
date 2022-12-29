


#include <iostream>
#include <vector>
#include
#include <algorithm>
using namespace std;

class Node{
  public:
    Node left;
    Node right;
    int value;
    inline Node(int val);
    addNode(int val);
};

inline Node::Node(int val){
  this->value = val;
}
Node::addNode(Node node, int val)


bool isSymmetric(vector<Node> tree)
{ 
  // check for 0 length, jumps to return true if size == 0
  if (tree.size() > 1){
    
  }
  return true;
}

int main(int argc, char const *argv[])
{
  // using a vector to link nodes will be traversed by their child nodes (left and right)
  vector<Node> Tree = {Node(69)}; // starting node

  return 0;
}
