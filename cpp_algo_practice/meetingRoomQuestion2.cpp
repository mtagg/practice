
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


class Meeting{
  public:
  int start;
  int end;

  Meeting(int s, int e);
};

Meeting::Meeting(int s, int e){
  this->start = s;
  this->end = e;
}

int meetingRooms(vector<Meeting> m){
  int nRooms = 0;
  vector<int> startTimes;
  vector<int> endTimes;

  //assume that there are equal start times and end times
  for (auto & meet : m){
    startTimes.push_back(meet.start);
    endTimes.push_back(meet.end);
  }
  
  sort( begin(startTimes), end(startTimes));
  sort( begin(endTimes), end(endTimes));

  auto s_itr = begin(startTimes);
  auto e_itr = begin(endTimes);


  ++nRooms; // we will always need at least 1 room if we have >0 meetings
  while (++s_itr != startTimes.end()){
    while ((*s_itr  < *e_itr) && (s_itr != startTimes.end())){
      ++nRooms;
      ++s_itr;
    }
    e_itr++;
  }
  
  return nRooms;
}
int main(int argc, char const *argv[])
{
  vector<Meeting> meets = { Meeting(10,12), 
                            Meeting(11,13), 
                            Meeting(12,14), 
                            Meeting(9,11), 
                            Meeting(9,11) 
                          };
  cout << meetingRooms(meets) << " room(s) are needed." << endl;

  return 0;
}
