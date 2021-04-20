from numpy import *

#Declaração de constantes
def calculo():
    angA = 0
    angB = 120
    angC = -120
    carga = 100
    Van = carga*exp(1j*deg2rad(angA))
    Za = 15 + 0j
    iA = Van/Za
    Vbn = carga*exp(1j*deg2rad(angB))
    Zb = 10 + 5j
    iB = Vbn/Zb
    Vcn = carga*exp(1j*deg2rad(angC))
    Zc = 6 - 8j
    iC = Vbn/Zb
    iN = iA + iB + iC

    print(iA, iB, iC, iN)



    print(iC)

    '''<img
     src=".\assets\trifasico.png"
     alt="Carga conectada em triângulo desequilibrada"
     width="500"
     height="500"
     >'''


