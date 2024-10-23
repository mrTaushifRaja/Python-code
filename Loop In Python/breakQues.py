# search for a number x in this tuples using loop

nums=(1,4,9,16,25,36,49,64,81,100)
X=36
idx=0  # intialization
while idx < len(nums):
  if(nums[idx]==X):
    print("found at idx",idx)   #nums[0],nums[1],nums[2]...
    break
  else:
    print("finding..")
  idx+=1
  
print("end of loop")