list1=input("enter list value:",)

copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
  print("palindrone")
else:
  print("not palindrone")
