pmt=input("payment:")
r= input("rate:")
t= input("time:")
n= input("frequency:")
rate_freq= int(r)/int(n)
c= rate_freq + 1
d= int(n)*int(t)
why= c**d
then= why - 1
f =then / rate_freq
a= int(pmt)* f
print("A is:", a)