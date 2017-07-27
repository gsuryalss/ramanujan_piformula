import math

#finds factorial for given number
def factorial(x):
    if x==0:
        return 1
    else:
        r=x*factorial(x-1)
        return r

#computes pi value by Ramanujan formula
#source : https://www.maa.org/sites/default/files/pdf/upload_library/22/Chauvenet/BorweinBorweinBailey.pdf
def pi_formula():
    sum = 0
    n = 0
    i = (math.sqrt(8))/9801

    while True:
        tmp = i*(factorial(4*n)/pow(factorial(n),4))*((26390*n+1103)/pow(396,4*n))
        sum +=tmp

        if(abs(tmp) < 1e-15):
            break
        n += 1

    return(1/sum)

print("Pi value using Ramanujan Formula : ",pi_formula())
