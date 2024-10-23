# WAP to enter of marks 3 subjectsfrom the user and store them in dictionary.
#stert with an emptydict & add one by one .use subject name as key & marks as vlaue.



marks= {}
x= int(input("Enter phy: "))
marks.update({"phy":x}),
  
x= int(input("Enter math: "))
marks.update({"math":x})
  
x= int(input("Enter chem: "))
marks.update({"chem":x})
  
print(marks)