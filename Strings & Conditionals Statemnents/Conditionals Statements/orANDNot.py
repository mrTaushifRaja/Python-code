A=int(input("A:"))
G=input("G/M:")
if((A==1 or A==3) and G=="M"):
    print("fee is 100")
elif((A==3 or A==4) and G=="M"):
    print("fee is 200")
elif(A==5 and G=="M" ):
    print("fee is 300")
else:
    print("no fee")