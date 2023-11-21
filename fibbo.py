def fibbo(n):
  if n <= 1:
    return fibbo(n-1) + fibbo(n-2)

def fibbo(n):
  n1 = 0
  n2 = 1
  count = 0
  if n == 1:
    return n1
  else:
    while count < n:
      print(n1)
      nth = n1 + n2
      n1 = n2
      n2 = nth
      count += 1
