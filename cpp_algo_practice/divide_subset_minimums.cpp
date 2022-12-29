

#include <iostream>
#include<vector>
using namespace std;

int sum(vector<int> vec){
  int sum = 0;
  for (int i = 0;  i < vec.size(); ++i){
    sum += vec.at(i);
  }
  return sum;
}

int divide_subset_minimums(int arr[], int n){

  int min, i;
  vector <int> subset1,subset2;
  subset1.push_back(arr[0]);
  subset2.push_back(arr[1]);
  for (i = 2; i < n; ++i){
    if (sum(subset1) < sum(subset2)){
      subset1.push_back(arr[i]);
    }else{
      subset2.push_back(arr[i]);
    }
  }
  return abs(sum(subset1)-sum(subset2));
}

int main(int argc, char const *argv[])
{
  int arr[] = {1,6,11,5};
  int n = sizeof(arr)/sizeof(int);
  cout<<divide_subset_minimums(arr,n);


  return 0;
}
