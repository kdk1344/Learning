def LL(st):
  st = st.replace(" ", "")
  a = list(st)
  b = a.reverse()
  if a == b:
    return True
  else:
    return False

LL('나는 나')

