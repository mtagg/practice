#include <iostream>
#include <string>

using namespace std;


int main(int argc, char const *argv[])
{
  string str_Arr [2];
  str_Arr[0] = "hello ";
  str_Arr[1] = "world!";
  // Appending two strings to print:
  cout<<str_Arr[0]+str_Arr[1]<<endl;
  // Iterating through string object to print:
  for (auto &c : str_Arr[0]){
    cout<<c;
  }
  for (auto &c : str_Arr[1]){
    cout<<c;
  }
  cout<<endl;
  return 0;
}
