

#include <iostream>
using namespace std;



void func(int A[], int B[], int N)
{
  int i, j, prod;
  for(i = 0; i < N; ++i){
    prod = 1;
    for (j = 0; j < N; ++j){
      if ( i!= j){
          prod *= A[j];
      }
    } 
    B[i] = prod;
  }
}


int main(int argc, char const *argv[])
{
  int A[] = {2,1,5,9};
  int N = sizeof(A)/sizeof(A[0]); 
  int B[N];
  func(A,B,N);
  
  for (int i = 0; i < N; ++i){
    cout<<B[i]<<" ";
  } 
  return 0;
}
