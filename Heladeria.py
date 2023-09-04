"""3)	Una heladería desea monitorear que tipo de sabores [especiales o tradicionales] son más populares entre sus clientes:
a.	Especiales: limón, maracuyá y frutos rojos
b.	Tradicionales: chocolate, vainilla y napolitano  
c.	Cada sorbete está conformado por la combinación de 2 sabores:
"""

# Dos especiales, resultan en, Sorbete especial
# Dos tradicionales, resultan en, Sorbete tradicional
# Uno de cada sabor, resultan en, Sorbete mixto

"""A su vez la heladeria ofrece los siguientes precios, con base al pedido del cliente

a) Por cada sorbete especial es $3.50
b) Por cada sorbete tradicional es $3.25
c) Por cada sorbete mixto es $3.75

¿Si Pepito tiene X amigos, cuanto será el total que obtendrá?

Mostrar cual fue el tipo de sorbete por cada amigo
Mostrar cuanto sorbetes pidio cada amigo
Mostrar cuanto fue el total por amigo
Nota: Si el total  excede los $15, mostrar en pantalla que Pepito solo pagará el 50%.
"""

# Declarando constantes

ESP = "Sorbete especial"
TRA = "Sorbete tradicional"
MIX = "Sorbete mixto"

ESPMONEY = 3.50
TRAMONEY = 3.25
MIXMONEY = 3.75

# Declarando variables

nom = "" #Esta variable es para nombre

sab1 = 0 #Este va a ser el primer sabor que escoga la persona
sab2 = 0 #Este va a ser el segundo sabor que escoga la persona

h = 0

lim1 = 0
lim2 = 0

numTipo = 0 #Esta variable es para mostrar el numero de sorbete por cliente

# Declarando interadores

i = 0
k = 0

# Declarando acumuladores

acuTipo = 0 #Acumulador de tipos de sorbetes
acuMoney = 0 #Acumulador de precio de tipo de sorbete
acuTotalMoney = 0 #Acumulador para el total de cada cliente

# Declarando vectores

vecNom = [] 
vecSab1 = [] #Este vector es para guardar el primer sabor 
vecSab2 = [] #Este vector es para guardar el segundo sabor
vecTipo = [] #Este vector es para guardar la combinacion resultante de los 2 sabores
vecMoney = []
j = [] #Este vector es para guardar el numero de sorbetes por amigo

#Nota: Los iteradores en FOR no se pueden repetir, esto porque en PYTHON, el FOR siempre reinicia
#El iterador

print("Heladeria del infierno")

h = int(input("\n¿Cuantos amigos tienes?: "))

#Ingreso de nombre

for i in range(h):
    vecNom.append(input("\nIngresa tu nombre amigo numero {}: ".format(i+1)))
    #Ingreso de cantidad de sorbetres
    j.append(int(input("\n¿Cuantos sorbetes queres comprar {}?: ".format(vecNom[i]))))

    #Validacion de cantidad de sorbetes a escoger
    while j[i] < 1 or j[i] > 10:
        print("\nHa ingresado un valor fuera del rango, intente otra vez")
        j[i] = int(input("¿Cuantos sorbetes queres comprar {}?: ".format(vecNom[i])))
    print("Valor aceptado\n")
    
    for k in range(j[i]):

        print("********************")
        print("Sorbete numero {}".format(k+1))
        print("********************")

        #Ingreso de combinacion de sorbetes
        print("\nMenu de sabores \nEspeciales: 1)limón, 2)maracuyá y 3)frutos rojos \nTradicionales: 4)chocolate, 5)vainilla y 6)napolitano ")
        print("\nElige tu combinacion de sabores")

        #Ingreso del primer sabor
        sab1 = int(input("\nIngresa el numero de tu primer sabor: "))
        while sab1 < 1 or sab1 > 6:
            print("\nHas ingresado un valor fuera del rango") 
            sab1 = int(input("Ingresa el numero de tu primer sabor: "))
        print("\nPrimer sabor aceptado uwu")

        #Ingreso del segundo sabor
        sab2 = int(input("\nIngresa el numero de tu segundo sabor: "))
        while sab2 < 1 or sab2 > 6:
            print("\nHas ingresado un valor fuera del rango") 
            sab2 = int(input("Ingresa el numero de tu segundo sabor: "))
        print("\nSegundo sabor aceptado uwu")


        #Ingreso de sabor al vector del PRIMER sabor

        if sab1 == 1:
            vecSab1.append("Tu sabor es Limon ")
        elif sab1 == 2:
            vecSab1.append("Tu sabor es Maracuyá ")
        elif sab1 == 3:
            vecSab1.append("Tu sabor es Frutos rojos ")
        elif sab1 == 4:
            vecSab1.append("Tu sabor es Chocolate ")           
        elif sab1 == 5:
            vecSab1.append("Tu sabor es Vainilla ")   
        else:
            vecSab1.append("Tu sabor es Napolitano")

        #Ingreso de sabor al vector del SEGUNDO sabor

        if sab2 == 1:
            vecSab2.append("Tu sabor es Limon ")
        elif sab2 == 2:
            vecSab2.append("Tu sabor es Maracuyá ")
        elif sab2 == 3:
            vecSab2.append("Tu sabor es Frutos rojos ")
        elif sab2 == 4:
            vecSab2.append("Tu sabor es Chocolate ")           
        elif sab2 == 5:
            vecSab2.append("Tu sabor es Vainilla ")   
        else:
            vecSab2.append("Tu sabor es Napolitano")
        
        #Ingreso de combinacion resultante al vector de TIPO

        #Ingreso de valores de precio segun tipo al vector MONEY

        if sab1 > 0 and sab1 < 4 and sab2 > 0 and sab2 < 4:
            vecTipo.append(ESP)
            vecMoney.append(ESPMONEY)
        elif sab1 > 3 and sab1 < 7 and sab2 > 3 and sab2 < 7 :
            vecTipo.append(TRA)
            vecMoney.append(TRAMONEY)
        else:
            vecTipo.append(MIX)
            vecMoney.append(MIXMONEY)

    print("---------------------------------------------------------------------------------------")
#--------------------------------------------------------------------------------------------------

print("\nImpresion de resultados")

print("\n-----------------------------------------------------------------------")

#Reinicio de la variable "i" por uso de while

i = 0

while i < len(vecNom):
    print("\nNombre de cliente {}: {}".format(i+1,vecNom[i] ))

    #Validacion del limite 1, para que cuando corra la segunda vuelta el FOR de abajo,
    #No empiece desde 0 otra vez y vuelva a imprimir los resultados desde el primer cliente

    if i == 0:
        lim1 = 0
        lim2 = j[i]
    else:
        lim1 = k + 1
        lim2 = j[i]+ k + 1
    
    #Impresion de tipo de sabor para cada sorbete
    #Impresion de cantidad de dinero 

    numTipo = 0

    for k in range(lim1, lim2):
        print("Tu tipo de sabor para tu helado {} es: {}".format(numTipo+1, vecTipo[k]))
        print("El costo para tu helado {} es: {}".format(numTipo+1,vecMoney[k]))
        acuMoney = acuMoney + vecMoney[k]
        numTipo = numTipo + 1


    print("El total de sorbetes para {} es: {}".format(vecNom[i],j[i]))
    print("El costo total para {} es: {} ".format(vecNom[i] ,acuMoney))
    acuTotalMoney = acuTotalMoney + acuMoney

    i += 1
    acuMoney = 0

if acuTotalMoney > 15:
    print("\nEl total a pagar por pepito dado que es más de $15 es: {}".format(acuTotalMoney/2))
else:
    print("\nEl total a pagar por pepito es: {}".format(acuTotalMoney))





