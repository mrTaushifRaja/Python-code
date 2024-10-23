marks = int(input("Studentd Of marks : "))
if(marks >= 90):
    print("grade A")
elif(marks >= 80 and marks <90):
    print("grade B")
elif(marks >= 60 and marks <80):
    print("grade C")
elif(marks >= 40 and marks <60):
    print("grade D")
else:
    print("fail E")