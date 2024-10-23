a=float(input("Enter a value"))
b=float(input("Enter a value"))
c=float(input("Enter a value"))

if(a>b and a>c):
  print("a is greater than all numbers:")
elif(b>a and b>c):
   print("b is greater than all numbers:")
elif(c>a and b>c):
   print("c is greater than all numbers:")
   
else:
  print("All number are aqual:")