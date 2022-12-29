
template<typename D, typename B>
#include <iostream>

class IsDerivedFromHelper{

  class No {};
  class Yes {No no[3];};

  static Yes Test(B*);
  static No Test();

  public:
   enum { Is = sizeof(Test(static_cast<D*>(0))) == sizeof(Yes) };
};

template <class C, class P>
bool isDerivedFrom(){
  return IsDerivedFromHelper<C,P>::Is;
}


// int main(int argc, char const *argv[])
// {
//   /* code */
//   return 0;
// }
