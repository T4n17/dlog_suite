import math

def GCD(a,b): #Function to compute the greatest common divisor between a and b
    while b != 0:
        a, b = b, a % b
    return a

def ElementOrder(x, p): #Function to compute the order of an element x in a group p
    n = GroupOrder(p)
    fact = PrimeFactorization(n)
    fact_set = list(set(fact))
    t = n
    for i in range(0, len(fact_set)-1):
        t = t // pow(fact_set[i], fact.count(fact_set[i]), p)
        x1 = pow(x,t,p)
        while x1 != 1:
            x1 = pow(x1, fact_set[i], p)
            t = t * fact_set[i]
    return t

def isPrime(p): #Function to check if a number p is prime
    for i in range(2, p-1):
        if p % i == 0:
            return False
        return True
    
def GroupOrder(n): #Function to compute the order of a group n
    if isPrime(n):
        return n-1
    fact = list(set(PrimeFactorization(n)))
    res = 1
    for f in fact:
        res = res * (f-1)  
    return res

def CRT(x, q, N): #Function to compute the remainder chinese theorem between a system of congruences x mod q, where N = q1*q2*q3*...qi
    res = 0
    for i in range(len(x)):
        x_i = x[i]
        q_i = q[i]
        n_i = N // q_i
        d,s,v = XGCD(n_i, q_i)
        res = res + (x_i * n_i * s)
    return res % N

def BSGS(g, h, p): #Baby-Step Giant-Step Algorithm to compute discrete logarithm of h in base g (mod p)
    L1 = []
    L2 = []
    n = 1 + round(math.sqrt(GroupOrder(p)))
    for x in range(n):
        L1.append(pow(g,x,p))
        L2.append((h*(pow(g,((-n)*x),p)) % p))
        for e1 in L1:
           if e1 in L2:
               return (L1.index(e1)) + ((L2.index(e1)) * n)
    return -1

def XGCD(a, b): #Function to compute the Extended Euclidean Algorithm between a and b
    if a == 0 : 
        return b,0,1

    gcd,x1,y1 = XGCD(b%a, a) 
     
    x = y1 - (b//a) * x1 
    y = x1 

    return gcd,x,y 

def PrimeFactorization(n): #Function to compute the prime factorization of n
    p = 2
    factors = []
    while p*p <= n:
        while (n % p) == 0:
            factors.append(p)
            n = n // p
        p = p + 1
    if n > 1:
       factors.append(p)
    return factors

def pollard_p(g,h,p): #Pollard Rho Algorithm to compute the discrete logarithm of h in base g (mod p)
    ord = ElementOrder(g,p)
    x = 1
    y = 1
    alpha = 0
    beta = 0
    gamma = 0
    delta = 0

    def randomWalk(x, e1, e2):
        if x >= 0 and x < (p // 3) :
           e1 = (e1 + 1) % ord
           return g*x % p, e1, e2
        elif x >= (p // 3) and x < (2*p // 3) :
           e1 = (e1*2) % ord
           e2 = (e2*2) % ord
           return x*x % p, e1, e2
        elif x >= (2*p // 3) and x < p :
           e2 = (e2+1) % ord
           return h*x % p, e1, e2
    
    while True:
        x, alpha, beta = randomWalk(x, alpha, beta)
        y, gamma, delta = randomWalk(y, gamma, delta)
        y, gamma, delta = randomWalk(y, gamma, delta)
        if x == y:
            break

    u = (alpha - gamma) % ord
    v = (delta - beta) % ord

    d,s,v = XGCD(v, ord)

    if d == 1 :
        return u*s % ord

    w = u*s % ord
    
    L = []

    for i in range(0,d):
        l = (w // d)+(i*(ord // d))
        if pow(g,l,p) == h:
            return l
    return -1

def pohlig_hellman(g, h, p): #Full Pohlig Hellman Algorithm to compute discrete logarithm of h in base g (mod p)
    ord = ElementOrder(g,p)
    f_order = PrimeFactorization(ord)
    x_list = []
    q_list = []
    a_list = []
    for i in range(0, len(f_order)):
        if f_order[i] not in a_list:
            q = f_order[i]
            e = f_order.count(f_order[i])
            exp = ord // q**e
            g2 = pow(g,exp,p)
            h2 = pow(h,exp,p)
            if e > 1:
                exp2 = pow(q,e-1,p)
                x0 = pollard_p(pow(g2,exp2,p), pow(h2,exp2,p), p)
                x_log = x0
                for x in range(2,e+2):
                    exp_h = pow(q,e-x,p)
                    exp_g = pow(q,e-1,p)
                    h_i = h2*(pow(g2,-x_log,p))
                    x_log = x_log + (pow(q,x-1,p))*(pollard_p(pow(g2,exp_g,p), pow(h_i,exp_h,p), p))
            else:
                x_log = pollard_p(g2,h2,p)
            x_list.append(x_log)
            q_list.append(q**e)
            a_list.append(q)
    return CRT(x_list, q_list, ord)
