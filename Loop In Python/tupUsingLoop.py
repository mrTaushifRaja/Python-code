#search for a num X in this tup Using Loop


nums=(1,4,9,25,36,49,64,81,100)
X=49 
idx=0
for val in nums:
    if(val==X):
      print("number found at idx",idx)
    idx+=1