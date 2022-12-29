




#include <iostream>

uint32_t longest_alt_evenodd_seq(int arr[], int n)

{
  uint32_t longest = 1;
  uint32_t current = 1;
  int i;
  for (i=1; i < n; i++)
  {
    if (arr[i-1]%2 != arr[i]%2){
      current+=1;
    }
    else{
      if (current > longest){
        longest = current;
        current = 1;
      }
    }
  }
  return (current > longest) ? current : longest;
}


int main(int argc, char const *argv[])
{
  int arr [] = {3,2,3,4,5,6,3,3,4,4,6,1,2,3,3,2,1,2,1,2,1,8,9,0};
  int n = sizeof(arr) / sizeof(arr[0]);
  std::cout << longest_alt_evenodd_seq(arr, n) << std::endl;
  return 0;
}
