p = input("principal: ")
t =  input("time: ")
r = input("rate: ")
dec = int(r) / 100
c = dec * int(t)
why = 1 + c
a = int(p) * why 
print("A is : ", a)
