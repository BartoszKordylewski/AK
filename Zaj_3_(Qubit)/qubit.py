import math
import itertools
class Complex(object):
    def __init__(self, real, imag=0.0):
        self.real = real
        self.imag = imag

    def __str__(self):
        return '(%g, %g)' % (self.real, self.imag)
    def __add__(self, other): #dodawanie
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other): #odeejmowanie
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __mul__(self, other): #mnozenie
        return Complex(self.real*other.real - self.imag*other.imag,
                       self.imag*other.real + self.real*other.imag)

    def __abs__(self): #warbez
        return math.sqrt(self.real**2 + self.imag**2)

    def __neg__(self):   #negacja
        return Complex(-self.real, -self.imag)

    def __eq__(self, other): #sprawdzenie czy rowne
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other): #nie rowne
        return not self.__eq__(other)

    def __truediv__(self, other):#dzielenie
        conjugation = Complex(other.real, -other.imag)
        denominatorRes = other * conjugation
        denominator = denominatorRes.real
        nominator = self * conjugation
        return Complex(nominator.real/denominator, nominator.imag/denominator)
    _floordiv_ = __truediv__
    def __pow__(self, power):

        pass
    def con(self): #sprezenie
        return Complex(self.real, -self.imag)
    def polar(self): #postaca tryg
        a= self.real
        b= self.imag
        radius = math.hypot(a,b)
        theta = math.atan2(b,a)
        ang = theta * 180/math.pi
        return round(radius,4),round(theta,4),round(ang,4)
class Vector(object):
    def __init__(self, *args):
        self.args = args
    def __repr__(self):
        return "{}".format(",".join(map(str, self.args[0])))
    def __add__(self, other):
        x = []
        z = 0
        for i in self.args[0]:
            x.append((i.real +other.args[0][z].real,i.imag + other.args[0][z].imag))
            z+=1
        for i in x:
            i = Complex(i[0],i[1])
        return Vector(x)
    def __mul__(self,other):
        x = []
        if isinstance(other,int):
            for i in self.args[0]:
                x.append((i.real * other,i.imag * other))
            return Vector(x)
        else:
            z = 0
            dotproduct = Complex(0,0)
            for i in self.args[0]:
                o_real = other.args[0][z].real
                o_imag = other.args[0][z].imag
                x.append(Complex(i.real*o_real - i.imag*o_imag,i.imag*o_real + i.real * o_imag))
                dotproduct.real += x[z].real
                dotproduct.imag += x[z].imag
                z+=1
        #print("Wynik to: {}".format(dotproduct))
        #return Vector(x)
        return dotproduct
    def norm(self):
        result = Complex(0,0)
        for i in self.args[0]:
            result.real += ((i.real*i.real)+(i.imag*i.imag))
        result.real = math.sqrt(result.real)
        return result
a = Complex(2,-3)
b = Complex(3,-2)
c = Complex(3,4)
d = Complex(2,-5)
e = Complex(0,0)
f= Complex(0,2.19328005074)
g = Complex(0,1)
z= [f,g]
x = [a,b,a]
y = [c,d,e]
v1 = Vector(x)
v2 = Vector(y)
v3 = Vector (z)
nor1= v3.norm()
sum = v1+v2
mul = (v1*v2)
toll = 4
skalar = v1*toll
nor = v1.norm()
"""
print("Liczba 1: " + str(a) + " Liczba 2: " + str(b))
print("Dodawanie: " + str(a+b)) #dodawanie
print("Odejmowanie: " +str(a-b)) #odejmowanie
print("Mnozenie: "+ str(a*b)) #mnozenie
print("Dzielenie: "+str(a/b)) #dzielenie
print("Wartosc bezwzgledna: "+str(abs(a))) #wartosc bezwzgledna
print("Sprezenie: "+str(a.con())) #sprezenie
print("Postac trygonometryczna: "+str(a.polar())) #postac tryg
print("Wektor v1: " + str(v1)+" Wektor v2: "+str(v2))
print("Suma wektorow: {}".format(sum))
print("Skalar wektora v1 przez liczbe {}:".format(skalar))
print("Iloczyn skalarny wektorow v1, v2: {}".format(mul))
#print("Iloczyn wektorow: {}".format(mul)) - wektor po zmianie"""
print("Norma wektora v1 to: {}".format(nor1))