P1 = True
P2 = True
P3 = True
P4 = False
P5 = False

rule1 = P1 and P2
rule2 = P1 and P2 and P3 and not P4
rule3 = P1 and P2 and P3 and not P4 and P5

if (rule3):
    print("The customer can rent SUV")
elif(rule2):
    print("Customer can rent Sedan")
elif(rule2):
    print("The Customer is not elligible")



def unification(a,b):
    if len(a) != len(b):
        return "Unification Failed"
    elif(a[0] != b[0]):
        return "Unification Failed"
    else:
        result = a[:2]
    
    for l in range(2,len(a)-1):
        result += a[l]
        if(a[l]==";"):
            continue
        result += "/"
        result += b[l]
        result += ")"

        print("Unification Success")
        return result
print("Enter Expression 1")
a = input()
print("Enter Expression 2")
b = input()
print(unification(a, b))