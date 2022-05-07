import json

print("a or b")
s0 = 0
s1={}
s2=[]
fun1 = input("enter function name:")
with open ("Q.json","r") as f :
    Q=json.loads(f.read())
    for i in Q:
        print (i)
        a = input ("enter the answer:")
        s2.append(a)
        if a == Q[i]:
            print('Good answer')
            s0=s0+1
        else :
            print('False')
            s0=s0-1

    s1 = {fun1:s2}
    print (s1)
    print('final:',s0)


            
        
        
