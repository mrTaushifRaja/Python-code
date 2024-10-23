# WAF to print the elements of a list in a single line. (list is the parameters)


cities=["delhi","mimbai","goa","pune","chennai","gurgaon"]
heroes=["thor","captain","ironman","shaktiman"]


def print_len(list):
  print(len(list))
  
def print_list(list):
  for item in list:
    print(item,end=" ")
 
print_list(heroes)
print()