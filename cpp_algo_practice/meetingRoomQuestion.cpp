#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Meeting{
  public:
    int startTime;
    int endTime;

    Meeting(int start,int end);
};

Meeting::Meeting(int start, int end){
  this->startTime = start;
  this->endTime = end;
}


int numberOfRooms(vector<Meeting> meetings){
  int min = 0;
  int numMeetings = meetings.size();
  
  int roomNumber = 0;
  int meetingRooms [numMeetings] = {roomNumber};
  
  if (!numMeetings){
    return 0;
  }else{
    roomNumber = 1;
    meetingRooms[0] = 1;
  }
  //sort(meetings.begin(),meetings.end());

  for (int i = 0; i < numMeetings; ++i){
    Meeting curr_m = meetings[i];
    for (int j = i+1; j < numMeetings; ++j){
      Meeting m = meetings[j];
      if (m.startTime < curr_m.endTime){
        
        if (meetingRooms[j] == 0 || meetingRooms[j] == meetingRooms[i]){
          roomNumber++;
          cout<<roomNumber<< " ";
          meetingRooms[j] = roomNumber;
          break;
        }
      }
      meetingRooms[j] = roomNumber;
      // cout<<meetingRooms[j]<<" ";
    }
    cout<<endl;
  }
  
  return (meetingRooms[2]);
}

int main(int argc, char const *argv[])
{
  Meeting m1 = Meeting(8,11);
  Meeting m2 = Meeting(9,10);
  Meeting m3 = Meeting(10,12);
  vector<Meeting> meetings{m1,m2,m3};
  cout<<numberOfRooms(meetings);
  return 0;
}
