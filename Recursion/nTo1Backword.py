def show(n):
  if(n==0):
    return
  print(n)
  show(n-1)
  print("END")
  
show(5)  #5,4,3,2,1