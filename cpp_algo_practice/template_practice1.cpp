
#include <iostream>
using namespace std;


template<typename T, typename U>
class is_same{
public:
  static cosnt bool value = false;
};

template <typename T>
class is_same<T,T>{
public:
  static const bool value = true;
};

template <class A, class B>
bool IsSameClass(){
  return is_same<A,B>::value;
}

int main(int argc, char const *argv[])
{
  int a,b;
  bool c;
  is_same<int,int>(3,2);
  
  cout<< <a,b>IsSameClass();
  return 0;
}
