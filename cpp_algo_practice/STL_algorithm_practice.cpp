


#include <vector>
#include <algorithm>
#include <iostream>


using namespace std;


int main(int argc, char const *argv[])
{
  vector<int> vect{1,2,3,4,5};
  sort(vect.begin(),vect.end());
  reverse(vect.begin(),vect.end());

  for (auto &item: vect){
    cout<<item<<" ";
  }
  return 0;
}
