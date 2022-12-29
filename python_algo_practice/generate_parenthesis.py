'''
Solutions:
https://gist.github.com/syphh/173172ec9a4a1376e5096a187ecbddc9
YouTube Video:
https://www.youtube.com/watch?v=Peq4GCPNC5c&t=2224s&ab_channel=freeCodeCamp.org
'''


def perms (n, unclosed, comb, result):
  if n == 0:
    if unclosed == 0:
      return
    elif unclosed == 1:
      result.append(comb+ ")")
    else:
      perms(n, unclosed-1, comb + ")", result)
  elif n > 0:
    perms(n-1, unclosed+1, comb + "(", result)
    if unclosed > 0:
      perms(n, unclosed-1, comb + ")", result)
  return



def main():
  result = []
  n = 5
  perms(n, 0, "", result)
  print(result)
  print("Number of correct permutations of " + str(n) + " parenthesis' is: "+ str(len(result)))
main()