import requests
import socket
import math
def get():
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip
mia = get()
print('IPアドレス :',mia)
iplo = socket.gethostbyname(socket.gethostname())
ma,mi,mu,me=mia.split('.')
print('最小公倍数 :',math.lcm(int(ma),int(mi),int(mu),int(me)))
print('最大公約数 :',math.gcd(int(ma),int(mi),int(mu),int(me)))
yu = mia.replace('.','')
y = int(yu)
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
prime = str(prime_factorize(y))
pr = prime.replace('[','').replace(']','')
print('素因数分解 :',pr)
