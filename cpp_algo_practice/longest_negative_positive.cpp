


#include <iostream>
using namespace std;

int longest_negative_positive_sequence(int arr[], int n){
  int longest = 1;
  int count = 1;

  for (int i = 1; i < n; i++){
    if (arr[i]*arr[i-1] < 0){
      //does 0 matter?
      count++;
    }
    else{
      if (count > longest){
        longest = count;
        count = 1;
      }
    }
  }


  return (count > longest) ? count : longest;
}

int main(int argc, char const *argv[])
{
  int arr[] = {-1,1,-3,3,3,2,-5,5,-6,7,-8,5};
  auto n = sizeof(arr) / sizeof(arr[0]);
  cout<<longest_negative_positive_sequence(arr,n)<<endl;
  return 0;
}
