'''
Solutions:
https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVlfX1hPaHRZZW84endGM3dZRDZtSngtVVluUXxBQ3Jtc0ttNHdpTzJMTDMwZ1g1Yko2NlNIem1lUmtNUnE4eGgtU052VjE0WXB0QkdxeTZhNGxYWnZJVzROR21BbWlLXzlnbXREaXhtUWpiTm05SThxQ3ZrMnFhc3pXbV9Wanc1U05FQllKcUQwZXJ1ZVhCNVRxbw&q=https%3A%2F%2Fgist.github.com%2Fsyphh%2F173172ec9a4a1376e5096a187ecbddc9&v=Peq4GCPNC5c
YouTube Video:
https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2224s&ab_channel=freeCodeCamp.org
'''



# Returns true if anagram found
# Anagram is where a word has the exact length and mode of each char0 
def isValidAnagram(str1,str2):
  if len(str1) == len(str2):
    s1 = sorted(list(str1))
    s2 = sorted(list(str2))
    for i in range(len(s1)):
      if s1[i] != s2[i]:
        return False
    return True
  return False

def main():
  str1 = "aabbccdd"
  str2 = "abcd"
  str3 = "ccddaabb"
  str4 = "adamiscool"
  str5 = "isadamcool"
  print(isValidAnagram(str1,str2))
  print(isValidAnagram(str1,str3))
  print(isValidAnagram(str2,str3))
  print(isValidAnagram(str4,str5))

main()
  
  