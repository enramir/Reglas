
"""
En primer lugar, voy a elegir los tres atributos, que creo, que son los que más influyeron a la hora de sobrevivir en el Titanic. Luego dividiré
el fichero en estos tres atributos.
-Edad
-Sexo
-Clase
Creo que tanto el destino, como la habitación, el ticket... son atributos que nos van a aportar muy poco.

"""
def abrirFichero():
    
    fichero = open('titanic.txt', "r")
    lista = []
    for ind,lin in enumerate(fichero):
        if(ind != 0): #me salto la primera línea del fichero
            lin = lin.replace('\"','') #Elimino las comillas
            lin = lin.replace('\n', '') #Elimino los saltos de líneas
            
            if "Southampton" in lin:
                lin = lin.replace("Southampton", "") 
            if ", jr" in lin:
                lin = lin.replace(", jr", "")
            if ", Jr. (Lily Alexenia Wilson)" in lin:
                lin = lin.replace(", Jr. (Lily Alexenia Wilson)", "")
            if ", Jr" in lin:
                    lin = lin.replace(", Jr", "")
            if ", E.)" in lin:
                lin = lin.replace(", E.)", "")
            
                
            lin = lin.split(",") #divido por comas
            lista.append(lin) 
           
    fichero.close()
    return lista

#print(abrirFichero())
"""
Ahora vamos a tratar los valores que tienes 'NA', y los vamos a tratar con dos técnicas. La primera, sustituir NA por el valor más frecuente en todos 
los ejemplos de la clase del ejemplo, y la segunda (sólo para valores numéricos) con la media aritmética.
Si nos damos cuenta, valores 'NA' sólo lo tenemos para la edad (lin[5]), luego vamos a hacer una media aritmética de todas las edades
de los pasajeros y sustituiremos esa media en donde haya 'NA'.
"""

def mediaAritmeticaEdad(fichero):
    cont = 0.
    cont2 = 0
    
    for lin in fichero:
        if(lin[5] != 'NA' and lin[5] != ''):
            #print(lin[5])
            cont += float(lin[5])
            
    for lin in fichero:
        if(lin[5] != 'NA'):
            cont2 += 1
            
     
    media_final = cont/cont2
    return media_final
    
#print(mediaAritmeticaEdad(abrirFichero()))

"""
A continuación a parte de cambiar el valor 'NA' por la media aritmética de la edad, que es de 31.02664031496063, vamos a cambiar a 
los pasajeros menores de 13 años le pondremos (-), y si tiene más de 13 años, le pondremos (+).

"""
def cambiarValorNA(media_edad, fichero):
    list = []
    for lin in fichero:
        if(lin[5] == 'NA'):
            lin[5] = media_edad

        try:
            if(float(lin[5]) <= 13):
                lin[5] = "-"
                list.append(lin)
                
            else:
                lin[5] = "+"
                list.append(lin)
        
        except ValueError:
            pass
    
    return list
    
    
#print(cambiarValorNA(mediaAritmeticaEdad(abrirFichero()) ,abrirFichero()))

"""
Para realizar el entrenamiento, la poda y la medida del rendimiento, necesitamos dividir el conjunto de datos en tres partes: entrenamiento,
validación y test. La proporción adecuada de datos que van a cada parte, según mi punto de vista, sería:
                       80% --> conjunto de entrenamiento, 10% --> validación y 10% --> test.

Hacemos los cálculos y serían el 80% de 1313 ejemplos, es decir 1051 pasajeros irían al conjunto de entrenamiento
y como el 10% de 1313 es 131, nos quedaría 131 para el ejemplo de validación y los otros 131 para el de test.

También, como nos dice en el enunciado que hay que procurar que la partición sea estratificada, es decir, que la proporción de los ejemplos 
según los distintos valores de los atributos debe de ser en cada parte, similar a la proporción en el total de ejemplos.   
Yo haría lo siguiente, dividiría 1051 ejemplos del conj de entrenamiento para coger pasajeros en proporción de las tres clases sociales
que había en el Titanic. Por lo que cogería el 80% de cada clase social, y como de la 1st hay 322 pasajeros, de 2nd 279 y 3rd 711. 
Le hacemos el 80% de cada conjunto hasta llegar a los 1051 y nos quedaría 258 de 1st clase, 223 de 2nd clase y 570 pasajero de 3rd clase.
Harían un total de 1051 pasajeros para el conjunto de entrenamiento. 

Dividimos los conjuntos en los tres atributos que hemos seleccionado antes, como creo que mejor determinan la supervivencia. (Edad, Sexo y Clase).

"""

def divisionFicheroEnConjuntos():
    
    list = (cambiarValorNA(mediaAritmeticaEdad(abrirFichero()) ,abrirFichero()))
    conjuntos = [[],[],[]]
    conjunto_entrenamiento = []
    conjunto_validacion = []
    conjunto_test = []
    
    #CONJUNTO DE ENTRENAMIENTO
    
    for lin in list:
        if(lin[1] == "1st"):#veo si por cada fila de la list, en la posición 1, que se encuentra la clase de los pasajeros, es clase "1st".
            if(len(conjuntos[0]) < 258):#tengo que llegar hasta 258 pasajeros.
                conjuntos[0].append(lin)
                list.remove(lin) #voy eliminando de la lista total, las líneas que voy añadiendo al conjunto de entrenamiento.
        elif(lin[1] == "2nd"):
            if(len(conjuntos[1]) < 223):
                conjuntos[1].append(lin)
                list.remove(lin)
        elif(lin[1] == "3rd"):
            if(len(conjuntos[2]) < 570):
                conjuntos[2].append(lin)
                list.remove(lin)
    
    for i in conjuntos:
        conjunto_entrenamiento.append(i)
    
    
    return conjunto_entrenamiento
    conjuntos = [[],[],[]] #actualizo de nuevo la variable conjuntos para ir guardando ahora cada conjunto de validación.
    
    #CONJUNTO DE VALIDACIÓN
    """
    Como sobran 64 pasajeros de la clase 1st, 56 de la clase 2nd y 141 de la clase 3rd, voy a dividir para los conjuntos de validación y de test
    de la clase 1st, 32 pasajeros para validación y 32 para test. Para la clase 2nd, 28 ejemplos para validación y 28 para test. Y por último 
    para la clase 3rd, 71 ejemplos para el conjunto de validación y 70 para el conjunto test.
    """
    for lin in list:
        if(lin[1] == "1st"):
            if(len(conjuntos[0]) < 32):
                conjuntos[0].append(lin)
                list.remove(lin) #voy eliminando de la lista total, las líneas que voy añadiendo al conjunto de validación.
        elif(lin[1] == "2nd"):
            if(len(conjuntos[1]) < 28):
                conjuntos[1].append(lin)
                list.remove(lin)
        elif(lin[1] == "3rd"):
            if(len(conjuntos[2]) < 71):
                conjuntos[2].append(lin)
                list.remove(lin)
    
    for i in conjuntos:
        conjunto_validacion.append(i)
    return conjunto_validacion
    
    conjuntos = [[],[],[]] #actualizo de nuevo la variable conjuntos para ir guardando ahora cada conjunto de test.
    
    #CONJUNTO TEST
    
    for lin in list:
        if(lin[1] == "1st"):
            if(len(conjuntos[0]) < 32):
                conjuntos[0].append(lin)
                list.remove(lin)
        elif(lin[1] == "2nd"):
            if(len(conjuntos[1]) < 28):
                conjuntos[1].append(lin)
                list.remove(lin)
        elif(lin[1] == "3rd"):
            if(len(conjuntos[2]) < 70):
                conjuntos[2].append(lin)
                list.remove(lin)
    
    for i in conjuntos:
        conjunto_test.append(i)
    return conjunto_test

    
    #print(conjunto_entrenamiento)
    #print(conjunto_validacion)
    #print(conjunto_test)
    
    
#print(divisionFicheroEnConjuntos())      


#Así debería de quedar con un formato análogo a los archivos de datos que se han proporcionado (votos.py o credito.py, por ejemplo).


atributos=[("Clase",['1st','2nd','3rd']),
           ("Edad",['+','-']),
           ("Sexo",['female','male'])]  

atributo_clasificación = 'Supervivencia'

clases=['1','0']



#----------------------------------------------------------------------------------------


