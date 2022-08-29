#Parte de las funciones
pares = []

def ProductoCartesiano(conj1):
  #Lista que se usará en las funciones de las relaciones
  cartesiano = []
  #Combina cada valor del primer conjunto que escogio el usuario y lo combina con el segundo
  for a in conj1:
    for b in conj1:
      cartesiano.append((a, b))
  return (cartesiano)

def MayorIgualQue(cartesiano):
    #Recorre todos los elementos de los pares ordenados
    for i in range (len(cartesiano)):
        #Checa que el primer valor del par ordenado sea mayor o igual al segundo
        if cartesiano[i][0]>=cartesiano[i][1]:
            pares.append(cartesiano[i])
    return (pares)

def MenorIgualQue(cartesiano):
    #Recorre todos los elementos de los pares ordenados
    for i in range (len(cartesiano)):
        if cartesiano[i][0]<=cartesiano[i][1]:
            pares.append(cartesiano[i])
    return (pares)
  
def Igual(cartesiano):
    #Recorre todos los elementos de los pares ordenados
    for i in range (len(cartesiano)):
        #Checa que el primer valor del par ordenado sea menor o igual al segundo
        if cartesiano[i][0]==cartesiano[i][1]:
            pares.append(cartesiano[i])
    return (pares)
  
def Multiplos(cartesiano):
    #Recorre todos los elementos de los pares ordenados
    for i in range (len(cartesiano)):
        #Checa que el primer valor del par ordenado sea igual al segundo
        if int(cartesiano[i][1]) % int(cartesiano[i][0]) == 0:
            pares.append(cartesiano[i])
    return (pares)

def Doble(cartesiano):
    #Recorre todos los elementos de los pares ordenados
    for i in range (len(cartesiano)):
        #Checa que el segundo valor del par ordenado sea el doble que el primero
        if (int(cartesiano[i][1]) / 2) == int(cartesiano[i][0]):
            pares.append(cartesiano[i])
    return (pares)
  
def RelacionTransitiva(pares):
    #Recorre todos los elementos de los pares que cumplen con la relación
    for a,b in pares:
        #Recorre todos los elementos de los pares que cumplen con la relación con otros parámetros
        for c,d in pares:
            #Condicional que checa que se cumple la relación
            if b == c and ((a,d) in pares):
                    return ("Verdadero")
            else:
              return ("Falso")
    return ("Falso")
  
def RelacionReflexiva(pares):
    #Recorre todos los elementos de los pares que cumplen con la relación
    for a,b in pares:
        #Condicional que checa si no se cumple la relación
        if a != b and ((a,b) in pares):
            return ("Falso")
    return ("Verdadero")
  
def RelacionSimetrica(pares):
    #Recorre todos los elementos de los pares que cumplen con la relación
    for a,b in pares:
        #Condicional que checa si no se cumple la relación
        if (b,a) not in pares:
            return ("Falso")
    return ("Verdadero")

def RelacionEquivalencia(Reflectiva, Simetrica, Transitiva):
    #Condicional que checa si se todos los valores de las anteriores 3 funciones son verdadero.
    if Reflectiva =="Verdadero" and Simetrica == "Verdadero" and Transitiva == "Verdadero":
      return ("Verdadero")
    else:
      return ("Falso")
              

