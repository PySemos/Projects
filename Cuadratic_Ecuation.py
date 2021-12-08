"""
This is a sencille module wich resolve cuadratic ecuations in Python

author: @PySemos

"""

def calculate(a,b=0,c=0):
    #Funtion wich implement the formula for resolve cuadratic ecuations
    D=((b**2)-4*a*c)
    try:
        assert D>=0
    except AssertionError:
        return "The ecuation don't have solutions in the Real number set"
    if D>=0:
        ret=((-b+(D**(1/2)))/(2*a),(-b-(D)**(1/2))/(2*a))
        if ret[0]==ret[1]:
            return ret[0]
        else:
            return ret
def remove_white_spaces(arg):
    #Function that recive one argument and that argument will be a string and this 'll remove the white spaces
    try:
        assert type(arg)==str
    except AssertionError:
        raise ValueError("The argument must be a string")
    ret=""
    for letter in arg:
        if letter==" ":
            continue
        ret+=letter
    return ret
def get_pot2(arg):
    #This function only verificate if the ecuation is a cuadratic expression
    for index in range(len(arg)):
        try:
            if arg[index].isalpha() and arg[index+1]=="^":
                if arg[index+2]=="2":
                    return True
                elif arg[index+2]=="1" or arg[index+2]=="0":
                    return True
                else:
                    return False
        except IndexError:
            return False
    return False
class CuadraticEcuation:
    """
        The class that implement all the logic
        in the resolution of cuadratic ecuations
        Attributes:
            a  =>  float
            b  =>  float
            c  =>  float
            variable  =>  str
            cant_var=>int
            ecuation=>str
        Methods:
            __init__=>"initialicer"
            set_variable=>" This find the variable and check if the variable match (There is one single variable)"
            set_coef=> "This have the same function as set_variable but this do it with the cpefficients, not with the variable"
            calculate => Calculate the solution (if it have)
            __str__  and __repr__=> The representations about the object
    """
    a=0
    b=0
    c=0
    oper=("+","-")
    def __init__(self,ecuation):
        ecuation=remove_white_spaces(ecuation)
        assert get_pot2(ecuation)
        self.ecuation=ecuation
        self.set_variable()
        self.set_coef()
        self.result=self.calculate()
    def set_variable(self):
        self.variable=""
        self.cant_var=0
        for index in self.ecuation:
            if index.isalpha():
                if len(self.variable)==1 and self.variable==index:
                    self.cant_var+=1
                    continue
                elif len(self.variable)==1 and self.variable!=index:
                    raise ValueError("The ecuation must to have one single variable")
                elif len(self.variable)==0:
                    self.cant_var+=1
                    self.variable=index
    def set_coef(self):
        numero=""
        if self.ecuation[0].isalpha():
            numero+="1 "
        for index in range(len(self.ecuation)):
            if self.ecuation[index].isdigit():
                if self.ecuation[index-1]=="^":
                    continue
                elif self.ecuation[index].isdigit():
                    numero+=self.ecuation[index]
            if self.ecuation[index] in ("+","-"):
                numero+=self.ecuation[index]
            elif self.ecuation[index]==".":
                numero+="."
            
            elif (self.ecuation[index].isalpha() or self.ecuation[index] in self.oper) and numero[-1]!=" ":
                numero+=" "
        numero=numero.split()
        if len(numero)==3:
            self.a=float(numero[0])
            self.b=float(numero[1])
            self.c=float(numero[2])
        elif len(numero)==2:
            if self.cant_var==2:
                self.a=float(numero[0])
                self.b=float(numero[1])
                self.c=0
            elif self.cant_var==1:
                self.a=float(numero[0])
                self.b=0
                self.c=float(numero[1])
    def calculate(self):
        return calculate(self.a,self.b,self.c)
    def __str__(self):
        return str(self.result)
    def __repr__(self):
        return str(self)
"""
Simple Example:

ecuacion="-2x^2+4x-3"

ec=CuadraticEcuation(ecuacion)

print(ec)

"""
