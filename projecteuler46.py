import sympy
z=[]
for i in range(1,1000):  
        z.append(sympy.prime(i))
a=3
while True:
    a+=2
    if not sympy.isprime(a):
        for i in list(filter(lambda x: x < a, z)):
            c=(((a-i)/2)**0.5)
            if c.is_integer():
                break
        else:
            print(a)
            break