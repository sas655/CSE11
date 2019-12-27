p=input()
q=input()
p=int(p)
q=int(q)
i=int(0)
carry=int(0)
while p!=0 or q!=0:
    m=p
    n=q
    while m!=0 and n!=0:
        if (m%10)+(n%10)+i>=10:
            carry+=1
            i=1
        else:
            i=0
        m=int(m/10)
        n=int(n/10)
    if carry==0:
        print("No carry operation.")
    elif carry==1:
        print("1 carry operation.")
    else:
        print(str(carry) +" carry operations.")
    p=input()
    q=input()
    p=int(p)
    q=int(q)
    i=int(0)
    carry=int(0)
