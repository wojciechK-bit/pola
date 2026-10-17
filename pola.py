import math
PI=math.pi
print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()
if inp == "a":
    print("ppBryl - a | vBryl - b")
    inp = input("inp: ").lower().strip()
    if inp == "a":
        print("ppSzecianu - x | ppProstopadloscianu - y")
        inp = input("inp: ").lower().strip() 
        if inp == "x":
            a = float(input("a = "))
            print(f"ppSzecianu o boku {a} = {6*a**2}")
        elif inp == "y":
            a = float(input("a = "))
            b = float(input("b = "))
            c = float(input("c = "))
            print(f"ppProstopadloscianu o bokach {a} {b} {c} = {2*a*b+2*b*c+2*c*a}")
        elif inp == "b":
            print("vSzecianu - a | vProstopadloscianu - c")
        inp = input("inp: ").lower().strip() 
        if inp == "a":
            a=float(input("a= "))
            print(f"vszecianu o oboku {a}= {a**3}")
    else:
        print("nie ma takiej komendy")
elif inp == "c":
    a=float(input("a ="))
    b=float(input("b= "))  
    c=float(input("c= "))
    print(f"vprostopadloscianu o dlugosciach {a} {b} {c} = {a*b*c}")

if inp == "b": 
    print("obwody fig plaskie - a | pp fig plaskich - b")
    inp = input("inp: ").lower().strip()
    if inp == "b":
        print("ppgraniastoslupa - a |  ppostroslupa - b")
        inp=input("inp: ").lower().strip()
        if inp == "a":
                Pp=float(input("Pp = "))
                Pb=float(input("Pb="))
                print(f"ppgraniastoslupa o podstawie {Pp} {Pb} = {Pp+Pp+Pb}")
    elif inp=="b":
        Pp= float(input("Pp = "))
        Pb= float(input("Pb = "))
        print(f"ppostroslpa o podstawach {Pp} {Pb}= {Pp+Pb}")
        
    elif inp == "a":
        print("obwodkola - a| obwodtrapezu - b")
        inp = input("inp: ").lower().strip()
    if inp=="b":
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        d= float(input("d = "))
        print(f"obwodtrapezu {a} {b} {c} {d}= {a+b+c+d}")
    elif inp== "a":
        r=float(input("r= "))
        print(f"obewodkola {PI} {r} ={2*PI*r}")
        
        print("Bryly - a | Plaskie - b")
inp = input("inp: ").lower().strip()
print("ppBryl - a | vBryl - i")
inp = input("inp: ").lower().strip()

    
    
