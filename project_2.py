p= input("principal:")
r= input("rate:")
t= input("time:")
n= input("frequency:")
rate_freq= int(r)/int(n)
c= rate_freq + 1
d= int(n)*int(t)
why= c**d
a= int(p)*why 
print("A is:", a)