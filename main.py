#Define the function that will solve the cubic with 3 reals roots (returns just one root)
def solveCubic(a,b,c,d):
    bracket1 = (-b**3)/(27*a**3) + (b*c)/(6*a**2) + (-d)/(2*a)
    bracket2 = (c)/(3*a)+(-b**2)/(9*a**2)
    bracket3 = (-b)/(3*a)
    x = (bracket1+(bracket1**2+bracket2**3)**(1/2))**(1/3) + (bracket1-(bracket1**2+bracket2**3)**(1/2))**(1/3) + bracket3
    x = str(x.real) #Make sure only the real part is returned
    line = "The root of the cubic is "+x
    return(line)

# Ask the user for their name and cubic
print("-------------------------------------------------------------------")
print("I can solve cubics with 3 real roots i.e. ax^3+bx^2+cx+d=0.")
print("-------------------------------------------------------------------")
name = input("What is your name?")
a = int(input("What is your a?"))
b = int(input("What is your b?"))
c = int(input("What is your c?"))
d = int(input("What is your d?"))

# Tell the user what you will do and make the output beautiful
line = "Hello "+name.capitalize()+", I will solve "+str(a)+"x^3+"+str(b)+"x^2+"+str(c)+"x+"+str(d)+"=0."
line = line.replace("+-","-")
line = line.replace(" 1x^3"," x^3")
line = line.replace(" -1x^3"," x^3")
line = line.replace("+1x^2","+x^2")
line = line.replace("-1x^2","-x^2")
line = line.replace("+1x","+x")
line = line.replace("-1x","-x")
print(line)

# Give them the answer
print(solveCubic(a,b,c,d))

#END
quit()
