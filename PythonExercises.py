#Menu
import string
import random
global lista


def menuprincipal():
    print("|==========================================|")
    print("|=============Menu principal===============|")
    print("|=1-opcion1=Numero Mayor                 ==|")
    print("|=2-opcion2=Vocales                      ==|")
    print("|=3-opcion3=Paga Por Horas de Trabajo    ==|")
    print("|=4-opcion4=Diferencia de edad           ==|")
    print("|=5-opcion5=Numeros Romanos              ==|")
    print("|=6-opcion6=Numero Ramdons               ==|")
    print("|=7-opcion7=salir                        ==|")
    print("|==========================================|")
    opcion = int(input("Digite una opcion:"))
    if opcion == 1:
        NumMayor()
    elif opcion == 2:
        Vocales()
    elif opcion == 3:
        PagoPorHora()
    elif opcion == 4:
        listaEdades()
    elif opcion == 5:
        NumRomanos()
    elif opcion == 6:
        RandomN()
    elif opcion == 7:
            salir = str(input("Desea salir, reponder si o no:"))
            if salir == "si":
                print("Fin del programa")
            elif salir == "no":
                menuprincipal()

def NumMayor():
    Ingreso1=int(input("Ingrese el primer numero: "))
    Ingreso2=int(input("Ingrese el segundo numero: "))
    Ingreso3=int(input("Ingrese el tercer numero: "))

    if Ingreso1>Ingreso2<Ingreso3:
        print("El numero mayor es: ",Ingreso1)
        print("")
        menuprincipal()
    if Ingreso1<Ingreso2>Ingreso3:
        print("El numero mayor es: ",Ingreso2)
        print("")
        menuprincipal()
    if Ingreso1<Ingreso2<Ingreso3:
        print("El numero mayor es: ",Ingreso3)
        print("")
        menuprincipal()
    if Ingreso1==Ingreso2==Ingreso3:
        print("Todos los numeros son Iguales")
        print("")
        menuprincipal()

def Vocales():
    listaDeVocales=["A","E","I","O","U"]
    listaLetras = []
    numVocal = int(input("Digite numeros del 1 al 5:"))
    if(numVocal>5):
        print("Error!,debes de ingresar un numero dentro del rango establecido:")
        Vocales()
    else:

        vocal = listaDeVocales[numVocal-1]
        listaLetras.append(vocal)
        decision=input("Desea agregar otro numero del 1 al 5?: ")

        while decision.upper()=="S":
            numVocal= int(input("Digite numeros del 1 al 5:"))
            vocal = listaDeVocales[numVocal-1]
            listaLetras.append(vocal)
            decision=input("Desea agregar otra numero del 1 al 5?")
            
        
        print("La oracion formada fue: ",listaLetras)
        print("")
        menuprincipal()

def PagoPorHora():
    PagoA=1000
    PagoB=1000
    PagoC=50000   
    print("|==========================================|")
    print("|=============Menu principal===============|")
    print("|=1-Analista A                           ==|")
    print("|=2-Analista B                           ==|")
    print("|=3-Analista C                           ==|")
    print("|=4-Salir                                ==|")
    print("|==========================================|")
    opcionAnalista = int(input("Digite una opcion:"))

    if(opcionAnalista==1):
        print("Analista de Clase A:")
        IngreH = int(input("Ingrese las horas trabajadas: "))
        print("Su pago total es de: ",IngreH*PagoA)
        print("")
        PagoPorHora()

    if(opcionAnalista==2):
        print("Analista de Clase B:")
        IngreH = int(input("Ingrese las horas trabajadas: "))
        print("Su pago total es de: ",IngreH*PagoB)
        print("")
        PagoPorHora()

    if(opcionAnalista==3):
        print("Analista de Clase c:")
        IngreH = int(input("Ingrese las horas trabajadas: "))
        print("Su pago total es de: ",IngreH*PagoC)
        print("")
        PagoPorHora()

    if(opcionAnalista==4):
        print("")
        menuprincipal()

    if(opcionAnalista==0)(opcionAnalista>=4):
        print("Ingrese un numero valido")
        PagoPorHora()

def listaEdades():
    listaDeEdades = []
    EdadMayor=""
    EdadMenor=""
    Contador=0
    Edades = int(input("Ingrese una edad: "))
    listaDeEdades.append(Edades)
    Contador=Contador+1
    decision=input("Desea agregar otra edad?: ")

    while decision.upper()=="S":
        Edades = int(input("Ingrese otra edad mas: "))
        listaDeEdades.append(Edades)
        Contador=Contador+1
        decision=input("Desea agregar otra edad?: ")
        
    EdadMayor=int(max(listaDeEdades))
    EdadMenor=int(min(listaDeEdades))
    if(Contador>9):
        print('La edad mayor ingresada es:',EdadMayor)
        print('La edad menor ingresada es:',EdadMenor)
        print('La diferencia de edad entre',EdadMayor ,'y',EdadMenor,' es de:',EdadMayor-EdadMenor)
        print(f"Las edades ingresadas son ",sorted(listaDeEdades)) 
         
        print("")  
        menuprincipal()
    else:
        print("La cantidad de edad por ingresar debe de ser mayor a 10")
        listaEdades()
    
    
def NumRomanos():
  
    listaDeNumRomanos=["I","II","III","IV","V","VI","VII","VIII","IX","X"]
    listaNumNatural = []
    numNatural = int(input("Digite un numero del 1 al 10:"))
    listaNumNatural.append(numNatural-1)
    print("El numero equivalente en numeros romanos es: "+listaDeNumRomanos[numNatural-1])
    decision=input("Desea agregar otro numero del 1 al 10?: ")

    while decision.upper()=="S":
        numNatural= int(input("Digite numeros del 1 al 10:"))
        listaNumNatural.append(numNatural-1)   
        print("El numero equivalente en numeros romanos es: "+listaDeNumRomanos[numNatural-1])
        decision=input("Desea agregar otra numero del 1 al 10?. [Si= S/NO=N]")   
        print("")
    menuprincipal()
    
def RandomN():
    
    print("|==========================================|")
    print("|=============Menu principal===============|")
    print("|=1-Generar numero aleatorio             ==|")
    print("|=2-Salir                                ==|")
    print("|==========================================|")
    decisionRand=int(input("Digite una opcion: "))

    if(decisionRand==1):
        while(decisionRand==1):
            Randi=random.sample(range(1,25),1)    
            print("El numero aleatorio generado es: ",Randi)
            decisionRand=int(input("Ingrese 1 si desea generar otro numero,de lo contrario,presione cualquier tecla:"))
        menuprincipal()   
    elif(decisionRand==2):
        menuprincipal()

menuprincipal()