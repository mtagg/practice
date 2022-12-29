

#include <iostream>
#include <vector>
using namespace std;


int main(int argc, char const *argv[])
{
  vector<int>vect = {1,2,3,4,5,6,7,8};
  // vect.push_back(1);
  int i = 0;
  for (auto iterator = vect.begin(); iterator != vect.end(); ++iterator)
  {
    
    cout<<"hi"<< *iterator << endl;
    cout<<vect[i++];
  }
  return 0;
}
