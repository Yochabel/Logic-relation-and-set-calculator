from tabulate import tabulate
import random

#Funiciones de Tablas
def AND(x, y): #Función de la disyunción
    tabland=[]
    for i in range(len(x)):
        tabland.append(x[i]and y[i])
    return tabland
def OR(x, y):#Funicion de la conjunción
    tablaor=[]
    for i in range(len(x)):
        tablaor.append(x[i] or y[i])
    return tablaor
def IMPLI(x, y):#Función de la Implicación
    tablaimpli=[]
    for i in range(len(x)):
        tablaimpli.append(not x[i]or y[i])
    return tablaimpli
def BICO(x, y):#Función del bicondicional
    tablabico=[]
    for i in range(len(x)):
        tablabico.append((not x[i]or y[i]) and (not y[i]or x[i]))
    return tablabico
def NOT(x):#Función del NOT
    tablanot=[]
    for i in range(len(x)):
        tablanot.append(not (x[i]))
    return tablanot
#Funciones de Conjuntos
def eliminarrepetidos (l1):
    l2=[]
    for i in l1:
        if i not in l2:
            l2.append(i)
    return l2
#Esta función realiza la interseccion de conjuntos
def intersección(lista1, lista2):
    inter=[]
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i]==lista2[j]:
                inter.append(lista1[i])
    return inter
#Esta función realiza la Union de conjuntos
def union(lista1,lista2):
    union=[]
    for i in range(len(lista1)):
        union.append(lista1[i])
    for j in range(len(lista2)):
        union.append(lista2[j])
    union=eliminarrepetidos(union)
    return union
#Esta función realiza la Diferencia de conjuntos
def diferencia(lista1,lista2):
    dif=[]
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            dif.append(lista1[i])
    return dif

#Esta función realiza la Productos de conjuntos
def ProductoCarteciano(lista1,lista2):
    par = [(x,y) for x in lista1 for y in lista2]
    return par
#Esta función realiza la Diferencia Simetrica de conjuntos
def diferenciaSimetrica(lista1,lista2):
    difSim=[]
    difSim.append(diferencia(lista1,lista2))
    difSim.append(diferencia(lista2,lista1))
    return difSim
#Esta función revisa si hay Contencion de un conjunto en otro
def contención(lista1,lista2):
    contador=0
    for i in range(len(lista1)):
        if lista1[i] in lista2:
            contador+=1
    if contador==len(lista2):
        return True
    else:
        return False
#Cuenta la cantidad de elementos, para saber la cardinalidad
def Cardinalidad(lista):
    contador=0
    for i in lista:
        contador+=1
    return contador
#Esta función realiza el Conjunto Potencia de alguno de los conjuntos
def conjuntoPotencia(lista):
  subsets = []
  for i in range(2**len(lista)):
    subset = []
    for k in range(len(lista)):
        a=i & 1<<k
        if a:
            subset.append(lista[k])#Va metiendo elementos para crear los subconjuntos
    subsets.append(subset)
  return subsets
def complemento(lista):
    compl=[]
    for i in range(1,101):
        compl.append(i)
    compl=diferencia(compl,lista)
    return compl
#Funciones de Relaciones
#Se genera el producto cartesiano a través de dos ciclos que van formando sub listas con lo pares y depues los mete a un conjunto completo
def ProductoCarteciano(lista1,lista2):
    par = []
    for x in lista1:
        for y in lista2:
             sublista=[]
             sublista.append(x)
             sublista.append(y)
             par.append(sublista)

    return par
#Se revisa par por par cuales cumplen la relación de igual y los que la tienen se guradan en una nueva lista
def relaciónigual(listacartesiano, cantielem):
    subconjunto=[]
    for i in range(cantielem*cantielem):
        if listacartesiano[i][0]== listacartesiano[i][1]:
            subconjunto.append(listacartesiano[i])
    return subconjunto
#Se revisa par por par cuales cumplen la relación de mayor y los que la tienen se guradan en una nueva lista
def relaciónmayor(listacartesiano, cantielem):
    subconjunto=[]
    for i in range(cantielem*cantielem):
        if listacartesiano[i][0]> listacartesiano[i][1]:
            subconjunto.append(listacartesiano[i])
    return subconjunto
#Se revisa par por par cuales cumplen la relación de menor y los que la tienen se guradan en una nueva lista
def relaciónmenor(listacartesiano, cantielem):
    subconjunto=[]
    for i in range(cantielem*cantielem):
        if listacartesiano[i][0]< listacartesiano[i][1]:
            subconjunto.append(listacartesiano[i])
    return subconjunto
#Se revisa par por par cuales cumplen la relación de menor o igual y los que la tienen se guradan en una nueva lista
def relaciónmenorigual(listacartesiano, cantielem):
    subconjunto=[]
    for i in range(cantielem*cantielem):
        if listacartesiano[i][0]<= listacartesiano[i][1]:
            subconjunto.append(listacartesiano[i])
    return subconjunto
#Se revisa par por par cuales cumplen la relación de mayor o igual y los que la tienen se guradan en una nueva lista
def relaciónmayorigual(listacartesiano, cantielem):
    subconjunto=[]
    for i in range(cantielem*cantielem):
        if listacartesiano[i][0]>= listacartesiano[i][1]:
            subconjunto.append(listacartesiano[i])
    return subconjunto
#A través de un ciclo for se compara si por todos los elementos en el subconjunto se encuentra un par donde esta el mismo elemento
def reflexividad ( subconjunto, cantielem):
    contador=0
    for i in subconjunto:
        if i[0]==i[1]:
            contador+=1

    if cantielem==contador:
        return True
    else:
        return False
#A través de dos ciclos fors se va revisando si el primer elemento de un par es igual al segundo de otro y si en ese mismo par el sgundo es igual al primero
def simetria ( subconjunto, cantielem):
    contador=0
    for i in subconjunto:
        for j in subconjunto:
            if i[0]==j[1] and i[1]==j[0]:
                    contador+=1

    if len(subconjunto)==contador:
        return True
    else:
        return False

    #En los dos primeros ciclos for se revisa que en el primar el segundo elemento sea igual al primero de otro par si es así entra a otro for que va a busacar otro par donde tenga el primer elemento del primer par y el segundo de el otro
def transitivo (subconjunto, cantielem):
    contador=0
    contador2=0

    for i in subconjunto:#[(1,2)(2,3)]
        for j in range(1,len(subconjunto)):
            if i[1]==subconjunto[j][0] :
                contador2+=1
                for a in subconjunto:
                    if i[0]==a[0] and subconjunto[j][1]==a[1] and i!=a:
                        contador+=1
                if contador==0:
                    return False
    if contador2==0:
        return False
    return True


a=eval(input("1.Calculadora de tablas de verdad\n2.Calculadora de conjuntos\n3.Calculadora de relaciones 4.Salir"))
while a != 4:


    if a==2:

        #En todas las funciones se manipula una lista con los elementos del conjunto para poder obtener los resultados de las opereciones
        #Aquí se checa que no se repitan elementos en los conjuntos

        #Pregunta al usario si lo quiere introducir los elementos de forma manual o que se auto-generen
        ingresarConjuntos=eval(input("¿Quiere introducir los conjuntos o que se generen de manera aletoria?(Ingresea 1 si los quiere ingresar manualmete y 0 los quiere aleatorios)"))
        #Se crean las listas donde se guradaran los elementos de los conjuntos
        listaconjuntos1=[]
        listaconjuntos2=[]
        #El usuario introduce los dos elementos de cada conjunto
        if ingresarConjuntos==1:
            cantidadElem1=eval(input("¿Cuantos elementos quiere en el conjunto A?"))
            cantidadElem2=eval(input("¿Cuantos elementos quiere en el conjunto B?"))
            for i in range(cantidadElem1):
                print("Del conjunto A ingrese el elemento num", i+1)
                elemConj1=eval(input())
                listaconjuntos1.append(elemConj1)
            for i in range(cantidadElem2):
                print("Del conjunto B ingrese el elemento num", i+1)
                elemConj2=eval(input())
                listaconjuntos2.append(elemConj2)
        #Se generean los elementos de forma aleatoroa con la funcio randit
        if ingresarConjuntos==0:
            cantidadElem1=eval(input("¿Cuantos elementos quiere en el primer conjunto?"))
            cantidadElem2=eval(input("¿Cuantos elementos quiere en el primer conjunto?"))
            for i in range(cantidadElem1):

                elemConj1=random.randint(0,100)
                listaconjuntos1.append(elemConj1)
            for i in range(cantidadElem2):

                elemConj2=random.randint(0,100)
                listaconjuntos2.append(elemConj2)
        print(listaconjuntos1)
        print(listaconjuntos2)
        print("Escoja una operacioón de conjuntos:")
        #Se hace un ciclo para que se muestre el menu continuamente
        menu=0
        while(menu!=18):
            menu=eval(input("1.Intersección A y B \n2.Union A y B\n3.Diferencia A-B\n4.Diferencia B-A\n5.Diferencia simetrica\n6.Complemento de A\n7.Complemento de B\n"
              "8.Producto cartesiano AxB\n9.Producto cartesiano BxA\n10.Producto cartesiano AxA\n11.Producto cartesiano BxB\n12.Conjunto potencia A\n13.Conjunto potencia B"
              "\n14.Cardinalidad de A\n15.Cardinalidad de B\n16.Contención de A en B\n17.Contención de B en A\n18.Exit"))
         #Dependiendo que escoja el usuario es la función que se realiza
            if menu==1:
                print(intersección(listaconjuntos1,listaconjuntos2))
            if menu==2:
                print(union(listaconjuntos1,listaconjuntos2))
            if menu==3:
                print(diferencia(listaconjuntos1,listaconjuntos2))
            if menu==4:
                print(diferencia(listaconjuntos2,listaconjuntos1))
            if menu==5:
                print(diferenciaSimetrica(listaconjuntos1,listaconjuntos2))
            if menu==6:
                print(complemento(listaconjuntos1))
            if menu==7:
                print(complemento(listaconjuntos2))
            if menu==8:
                print(ProductoCarteciano(listaconjuntos1,listaconjuntos2))
            if menu==9:
                 print(ProductoCarteciano(listaconjuntos2,listaconjuntos1))
            if menu==10:
                 print(ProductoCarteciano(listaconjuntos1,listaconjuntos1))
            if menu==11:
                 print(ProductoCarteciano(listaconjuntos2,listaconjuntos2))
            if menu==12:
                print(conjuntoPotencia(listaconjuntos1))
            if menu==13:
                print(conjuntoPotencia(listaconjuntos2))
            if menu==14:
                print(Cardinalidad(listaconjuntos1))
            if menu==15:
                print(Cardinalidad(listaconjuntos2))
            if menu==16:
                print(contención(listaconjuntos1,listaconjuntos2))
            if menu==17:
                print(contención(listaconjuntos2,listaconjuntos1))
            if menu==18:
                a=eval(input("1.Calculadora de tablas de verdad\n2.Calculadora de conjuntos\n3.Calculadora de relaciones \n4.Salir"))


    if a==3:
        #Descripcion calculadora
        print('Calculadora de relaciones\n')
        print('''Esta calculadora funciona únicamente con 1 conjunto con cardinalidad de 0 a 20.
        Los elementos se deberán mantener dentro del rango de 1 a 100.\n''')
        print('Opciones para generar los conjuntos:\n\t1. Manualmente\n\t2. Aleatoriamente')
        ingresarConjuntos=eval(input("\nIntroduzca la opción deseada para generar los conjuntos: "))

        listaconjuntos1=[]
        #Indica la modalidad que se utilizara, si manual o random
        if ingresarConjuntos==1:
            print('Los elementos se introducirán manualmente.\n')
            cantidadElem1=eval(input("¿Cuántos elementos tiene el conjunto A? "))
            print('\nConjunto A')
            for i in range(cantidadElem1):
                print("Ingrese el elemento", i+1)
                elemConj1=eval(input())
                listaconjuntos1.append(elemConj1)

        if ingresarConjuntos==2:
            print('Los elementos se generarán de forma aleatoria.\n')
            cantidadElem1=eval(input("¿Cuántos elementos tiene el conjunto A? "))
            for i in range(cantidadElem1):
                elemConj1=random.randint(0,100)
                listaconjuntos1.append(elemConj1)

        lista=(ProductoCarteciano(listaconjuntos1,listaconjuntos1))
        print('\nConjunto:',listaconjuntos1)

        #Menú de operaciones
        print("Menú de operaciones de conjuntos:")
        print(" 1.Producto cartesiano\n2.Relación igual '='\n3.Relación mayor '>'\n4.Relación menor '-'\n5.Relación mayor igual '>='\n6.Relación menor igual '<='\n"
            "\n7.Exit")
        print('_ '*50)
        menu = 0
        while(menu!=7):
            menu=eval(input("Ingrese el número de la operación de conjuntos que quiere realizar: "))
            print()
            if menu==1:
                print('\tConjunto:',listaconjuntos1)
                print('\n\tProducto cartesiano AxB =',ProductoCarteciano(listaconjuntos1,listaconjuntos1),'\n')
                print('_ '*50)
            if menu==2:
                print('\tConjunto:',listaconjuntos1)
                subconjuntoigual=relaciónigual(lista,cantidadElem1)
                print('\n\tRelación igual =',subconjuntoigual,'\n')

                print('\n\t¿Es simétrica? ',simetria(subconjuntoigual,cantidadElem1),'\n')
                print('\n\t¿Es reflexiva? ',reflexividad(subconjuntoigual,cantidadElem1),'\n')
                print('\n\t¿Es transitiva? ',transitivo(subconjuntoigual,cantidadElem1),'\n')
                print('_ '*50)
            if menu==3:
                print('\tConjunto:',listaconjuntos1)
                subconjuntomayor=relaciónmayor(lista,cantidadElem1)
                print('\n\tRelación mayor =',subconjuntomayor,'\n')
                print('\n\t¿Es simétrica? ',simetria(subconjuntomayor,cantidadElem1),'\n')
                print('\n\t¿Es reflexiva? ',reflexividad(subconjuntomayor,cantidadElem1),'\n')
                print('\n\t¿Es transitiva? ',transitivo(subconjuntomayor,cantidadElem1),'\n')
                print('_ '*50)
            if menu==4:
                print('\tConjunto:',listaconjuntos1)
                subconjuntomenor=relaciónmenor(lista,cantidadElem1)
                print('\n\tRelación menor =',relaciónmenor(lista,cantidadElem1),'\n')
                print('\n\t¿Es simétrica? ',simetria(subconjuntomenor,cantidadElem1),'\n')
                print('\n\t¿Es reflexiva? ',reflexividad(subconjuntomenor,cantidadElem1),'\n')
                print('\n\t¿Es transitiva? ',transitivo(subconjuntomenor,cantidadElem1),'\n')
                print('_ '*50)
            if menu==5:
                print('\tConjunto:',listaconjuntos1)
                subconjuntomayorigual=relaciónmayorigual(lista,cantidadElem1)
                print('\n\tRelación mayor igual =',relaciónmayorigual(lista,cantidadElem1),'\n')
                print('\n\t¿Es simétrica? ',simetria(subconjuntomayorigual,cantidadElem1),'\n')
                print('\n\t¿Es reflexiva? ',reflexividad(subconjuntomayorigual,cantidadElem1),'\n')
                print('\n\t¿Es transitiva? ',transitivo(subconjuntomayorigual,cantidadElem1),'\n')
                print('_ '*50)

            if menu==6:
                print('\tConjunto:',listaconjuntos1)
                subconjuntomenorigual=relaciónmenorigual(lista,cantidadElem1)
                print('\n\tRelación menor igual =',relaciónmenorigual(lista,cantidadElem1),'\n')
                print('\n\t¿Es simétrica? ',simetria(subconjuntomenorigual,cantidadElem1),'\n')
                print('\n\t¿Es reflexiva? ',reflexividad(subconjuntomenorigual,cantidadElem1),'\n')
                print('\n\t¿Es transitiva? ',transitivo(subconjuntomenorigual,cantidadElem1),'\n')
                print('_ '*50)

            if menu==7:
                a=eval(input("1.Calculadora de tablas de verdad\n2.Calculadora de conjuntos\n3.Calculadora de relaciones \n4.Salir"))


            if (menu>11 or menu==0):
                print('\nOpción no disponible.\nIngrese una opción válida.\n')
                print('_ '*50)
        print('Fin de la operación.')
    if a==1:
        contador=1
        while(contador!=5):
            contador=int (input("MENU \n1.Tablas de verdad \n2.Verificar si 2 proposiciones compuestas son lógicamente equivalentes.\n3.Proposición es tautologia o contradicción.\n4.Instructivo\n5.Exit"))
            if contador==1:
                #ingresa la proposición
                prop=input("ingrese su proposición:")
                """prop.replace("p", "0")
                prop.replace('q', '1')
                prop.replace('r', '2')"""

                p=[True,True, False, False] #Valores que pueden tomar p, q ,r y las negaciones de estás
                q=[True,False,True,False]

                p1=[True,True,False,False,True,True, False,False]
                q1=[True,False,True,False,True,False,True,False]
                r1=[True,True,True,True,False,False,False,False]

                #Convierte la proposición a lista
                listaprop=list(prop.split(" "))
                #Genera la lista que se utilizara para imprimir los titulos de la tabla
                listapropheader=[]
                headers=[]
                for elemprop in listaprop:
                    listapropheader.append(elemprop)
                if 'p' in listaprop:
                    headers. append('p')
                if 'q' in listaprop:
                    headers. append('q')
                if 'r' in listaprop:
                    headers. append('r')
                estring=''
                estring2=''
                elemheders=0
                str2=0
                while (elemheders < (len(listapropheader))):
                    if (listapropheader[elemheders] == '~' and listapropheader[elemheders+1]=='(' and len(listapropheader) > 6):
                        while(listapropheader[str2]!=')'):
                            estring2=estring2+listapropheader[str2]
                            str2+=1
                    if (listapropheader[elemheders] == ')'):
                            for elemheaders1 in range(listapropheader.index('('), elemheders+1):
                                estring=estring+listapropheader[elemheaders1]
                            for elemheaders1 in range(listapropheader.index('('), elemheders+1):
                                if (listapropheader[elemheaders1]=='~'):
                                    headers.append(str (listapropheader[elemheaders1]+listapropheader[elemheaders1+1]))
                                    listapropheader.pop(elemheaders1)
                                    listapropheader.pop(elemheaders1)
                            del listapropheader[listapropheader.index('('):listapropheader.index(')')+1]
                            headers.append(estring)
                            estring=''
                            elemheders=0
                            elemheders-=1

                    if len(listapropheader)<=3:
                        elemheders=len(listapropheader)+1

                    elemheders+=1
                if len(estring2)!=0 and estring!=prop:
                    headers.append(estring2)
                headers.append(prop)

                #Listas para evaluar y guardar los datos
                listaeval=[]
                listalistas=[]
                #Identifia si hay r en la proposición para saber las combinaciones de verdadero y falso necesarias
                if 'r' in listaprop:
                    for pl1 in range(len(listaprop)):
                        if listaprop[pl1]=='p':
                            listaprop.insert(pl1,0)
                            listaprop.pop(pl1+1)

                    for ql1 in range(len(listaprop)):
                        if listaprop[ql1]=='q':
                            listaprop.insert(ql1,1)
                            listaprop.pop(ql1+1)

                    for rl1 in range(len(listaprop)):
                        if listaprop[rl1]=='r':
                            listaprop.insert(rl1,2)
                            listaprop.pop(rl1+1)
                    listalistas.append(p1)
                    listalistas.append(q1)
                    listalistas.append(r1)

                    #Evalua las primitivas para poder meter su valor en la lista que guardara todo los resultados



                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval.index('('), len(listaeval)-1):
                                if (listaeval[i]=='~'):
                                    listalistas.append(NOT (listalistas[int (listaeval[ i + 1])]))
                                    listaeval.insert(i,len(listalistas)-1)
                                    listaeval.pop(i+1)
                                    listaeval.pop(i+1)

                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval.index('('), len(listaeval)-1):

                                if(listaeval[j]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)

                                elif(listaeval[j]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='<>'):
                                    listalistas.append(BICO(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval) > 1:
                        for elem2 in range(len(listaeval)-1):
                            if(listaeval[elem2]=='~'):
                                listalistas.append(NOT(listalistas[int (listaeval[elem2+1])]))
                                listaeval.insert(elem2,len(listalistas)-1)
                                listaeval.remove(listaeval[elem2 + 1])
                                listaeval.remove(listaeval[elem2 + 1])
                        for elem3 in range(len(listaeval)-1):
                            if(listaeval[elem3]=='y'):
                                listalistas.append(AND(listalistas[int(listaeval[elem3-1])] , listalistas[int(listaeval[elem3 + 1])]))
                                listaeval.insert(elem3,len(listalistas)-1)
                                listaeval.pop(elem3-1)
                                listaeval.pop(elem3)
                                listaeval.pop(elem3)

                        for elem4 in range(len(listaeval)-1):
                                if(listaeval[elem4]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[elem4-1])] , listalistas[int(listaeval[elem4 + 1])]))
                                    listaeval.insert(elem4,len(listalistas)-1)
                                    listaeval.pop(elem4-1)
                                    listaeval.pop(elem4)
                                    listaeval.pop(elem4)

                        for elem5 in range(len(listaeval)-1):
                                if(listaeval[elem5]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem5-1])] , listalistas[int(listaeval[elem5 +1])]))
                                    listaeval.insert(elem5,len(listalistas)-1)
                                    listaeval.pop(elem5 -1)
                                    listaeval.pop(elem5)
                                    listaeval.pop(elem5)

                        for elem6 in range(len(listaeval)-1):
                                if(listaeval[elem6]=='<>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem6-1])] , listalistas[int(listaeval[elem6 +1])]))
                                    listaeval.insert(elem6,len(listalistas)-1)
                                    listaeval.pop(elem6 -1)
                                    listaeval.pop(elem6)
                                    listaeval.pop(elem6)


                else:
                    for pl in range(len(listaprop)):
                        if listaprop[pl]=='p':
                            listaprop.insert(pl,0)
                            listaprop.pop(pl+1)

                    for ql in range(len(listaprop)):
                        if listaprop[ql]=='q':
                            listaprop.insert(ql,1)
                            listaprop.pop(ql+1)
                    listalistas.append(p)
                    listalistas.append(q)
                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval.index('('), len(listaeval)-1):
                                if (listaeval[i]=='~'):
                                    listalistas.append(NOT (listalistas[int(listaeval[ i + 1])]))
                                    listaeval.insert(i,len(listalistas)-1)
                                    listaeval.pop(i+1)
                                    listaeval.pop(i+1)
                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval.index('('), len(listaeval)-1):

                                if(listaeval[j]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)

                                elif(listaeval[j]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[j-1])] , listalistas[(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='<>'):
                                    listalistas.append(BICO(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval) > 1:
                        for elem2 in range(len(listaeval)-1):
                            if(listaeval[elem2]=='~'):
                                listalistas.append(NOT(listalistas[int(listaeval[elem2+1])]))
                                listaeval.insert(elem2,len(listalistas)-1)
                                listaeval.remove(listaeval[elem2 + 1])
                                listaeval.remove(listaeval[elem2 + 1])
                        for elem3 in range(len(listaeval)-1):
                                if(listaeval[elem3]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[elem3-1])] , listalistas[int(listaeval[elem3 + 1])]))
                                    listaeval.insert(elem3,len(listalistas)-1)
                                    listaeval.pop(elem3-1)
                                    listaeval.pop(elem3)
                                    listaeval.pop(elem3)

                        for elem4 in range(len(listaeval)-1):
                                if(listaeval[elem4]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[elem4-1])] , listalistas[int(listaeval[elem4 + 1])]))
                                    listaeval.insert(elem4,len(listalistas)-1)
                                    listaeval.pop(elem4-1)
                                    listaeval.pop(elem4)
                                    listaeval.pop(elem4)



                        for elem5 in range(len(listaeval)-1):
                                if(listaeval[elem5]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem5-1])] , listalistas[int(listaeval[elem5 +1])]))
                                    listaeval.insert(elem5,len(listalistas)-1)
                                    listaeval.pop(elem5 -1)
                                    listaeval.pop(elem5)
                                    listaeval.pop(elem5)

                        for elem6 in range(len(listaeval)-1):
                                if(listaeval[elem6]=='<>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem6-1])] , listalistas[int(listaeval[elem6 +1])]))
                                    listaeval.insert(elem6,len(listalistas)-1)
                                    listaeval.pop(elem6 -1)
                                    listaeval.pop(elem6)
                                    listaeval.pop(elem6)

                dicparaimprimir={}
                for elemdic in range(len(listalistas)):
                    dicparaimprimir[headers[elemdic]]=listalistas[elemdic]

                print(tabulate(dicparaimprimir, headers))









            if contador==2:
                       #ingresa la proposición
                prop=input("ingrese su proposición:")
                prop2=input("ingrese su segunda proposición:")


                p=[True,True, False, False] #Valores que pueden tomar p, q ,r y las negaciones de estás
                q=[True,False,True,False]

                p1=[True,True,False,False,True,True, False,False]
                q1=[True,False,True,False,True,False,True,False]
                r1=[True,True,True,True,False,False,False,False]

                #Convierte la proposición a lista
                listaprop=list(prop.split(" "))
                listaprop2=list(prop2.split(" "))

                listaeval=[]
                listalistas=[]
                listaeval2=[]
                listalistas2=[]


                #Identifia si hay r en la proposición para saber las combinaciones de verdadero y falso necesarias
                if 'r' in listaprop:
                    for pl1 in range(len(listaprop)):
                        if listaprop[pl1]=='p':
                            listaprop.insert(pl1,0)
                            listaprop.pop(pl1+1)

                    for ql1 in range(len(listaprop)):
                        if listaprop[ql1]=='q':
                            listaprop.insert(ql1,1)
                            listaprop.pop(ql1+1)

                    for rl1 in range(len(listaprop)):
                        if listaprop[rl1]=='r':
                            listaprop.insert(rl1,2)
                            listaprop.pop(rl1+1)
                    listalistas.append(p1)
                    listalistas.append(q1)
                    listalistas.append(r1)

                    #Evalua las primitivas para poder meter su valor en la lista que guardara todo los resultados



                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval.index('('), len(listaeval)-1):
                                if (listaeval[i]=='~'):
                                    listalistas.append(NOT (listalistas[int (listaeval[ i + 1])]))
                                    listaeval.insert(i,len(listalistas)-1)
                                    listaeval.pop(i+1)
                                    listaeval.pop(i+1)

                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval.index('('), len(listaeval)-1):

                                if(listaeval[j]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)

                                elif(listaeval[j]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='<>'):
                                    listalistas.append(BICO(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval) > 1:
                        for elem2 in range(len(listaeval)-1):
                            if(listaeval[elem2]=='~'):
                                listalistas.append(NOT(listalistas[int (listaeval[elem2+1])]))
                                listaeval.insert(elem2,len(listalistas)-1)
                                listaeval.remove(listaeval[elem2 + 1])
                                listaeval.remove(listaeval[elem2 + 1])
                        for elem3 in range(len(listaeval)-1):
                            if(listaeval[elem3]=='y'):
                                listalistas.append(AND(listalistas[int(listaeval[elem3-1])] , listalistas[int(listaeval[elem3 + 1])]))
                                listaeval.insert(elem3,len(listalistas)-1)
                                listaeval.pop(elem3-1)
                                listaeval.pop(elem3)
                                listaeval.pop(elem3)

                        for elem4 in range(len(listaeval)-1):
                                if(listaeval[elem4]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[elem4-1])] , listalistas[int(listaeval[elem4 + 1])]))
                                    listaeval.insert(elem4,len(listalistas)-1)
                                    listaeval.pop(elem4-1)
                                    listaeval.pop(elem4)
                                    listaeval.pop(elem4)

                        for elem5 in range(len(listaeval)-1):
                                if(listaeval[elem5]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem5-1])] , listalistas[int(listaeval[elem5 +1])]))
                                    listaeval.insert(elem5,len(listalistas)-1)
                                    listaeval.pop(elem5 -1)
                                    listaeval.pop(elem5)
                                    listaeval.pop(elem5)

                        for elem6 in range(len(listaeval)-1):
                                if(listaeval[elem6]=='<>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem6-1])] , listalistas[int(listaeval[elem6 +1])]))
                                    listaeval.insert(elem6,len(listalistas)-1)
                                    listaeval.pop(elem6 -1)
                                    listaeval.pop(elem6)
                                    listaeval.pop(elem6)


                else:
                    for pl in range(len(listaprop)):
                        if listaprop[pl]=='p':
                            listaprop.insert(pl,0)
                            listaprop.pop(pl+1)

                    for ql in range(len(listaprop)):
                        if listaprop[ql]=='q':
                            listaprop.insert(ql,1)
                            listaprop.pop(ql+1)
                    listalistas.append(p)
                    listalistas.append(q)
                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval.index('('), len(listaeval)-1):
                                if (listaeval[i]=='~'):
                                    listalistas.append(NOT (listalistas[int(listaeval[ i + 1])]))
                                    listaeval.insert(i,len(listalistas)-1)
                                    listaeval.pop(i+1)
                                    listaeval.pop(i+1)
                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval.index('('), len(listaeval)-1):

                                if(listaeval[j]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)

                                elif(listaeval[j]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[j-1])] , listalistas[(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='<>'):
                                    listalistas.append(BICO(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval) > 1:
                        for elem2 in range(len(listaeval)-1):
                            if(listaeval[elem2]=='~'):
                                listalistas.append(NOT(listalistas[int(listaeval[elem2+1])]))
                                listaeval.insert(elem2,len(listalistas)-1)
                                listaeval.remove(listaeval[elem2 + 1])
                                listaeval.remove(listaeval[elem2 + 1])
                        for elem3 in range(len(listaeval)-1):
                                if(listaeval[elem3]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[elem3-1])] , listalistas[int(listaeval[elem3 + 1])]))
                                    listaeval.insert(elem3,len(listalistas)-1)
                                    listaeval.pop(elem3-1)
                                    listaeval.pop(elem3)
                                    listaeval.pop(elem3)

                        for elem4 in range(len(listaeval)-1):
                                if(listaeval[elem4]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[elem4-1])] , listalistas[int(listaeval[elem4 + 1])]))
                                    listaeval.insert(elem4,len(listalistas)-1)
                                    listaeval.pop(elem4-1)
                                    listaeval.pop(elem4)
                                    listaeval.pop(elem4)



                        for elem5 in range(len(listaeval)-1):
                                if(listaeval[elem5]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem5-1])] , listalistas[int(listaeval[elem5 +1])]))
                                    listaeval.insert(elem5,len(listalistas)-1)
                                    listaeval.pop(elem5 -1)
                                    listaeval.pop(elem5)
                                    listaeval.pop(elem5)

                        for elem6 in range(len(listaeval)-1):
                                if(listaeval[elem6]=='<>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem6-1])] , listalistas[int(listaeval[elem6 +1])]))
                                    listaeval.insert(elem6,len(listalistas)-1)
                                    listaeval.pop(elem6 -1)
                                    listaeval.pop(elem6)
                                    listaeval.pop(elem6)

                if 'r' in listaprop2:
                    for pl1 in range(len(listaprop2)):
                        if listaprop2[pl1]=='p':
                            listaprop2.insert(pl1,0)
                            listaprop2.pop(pl1+1)

                    for ql1 in range(len(listaprop2)):
                        if listaprop2[ql1]=='q':
                            listaprop2.insert(ql1,1)
                            listaprop2.pop(ql1+1)

                    for rl1 in range(len(listaprop2)):
                        if listaprop2[rl1]=='r':
                            listaprop2.insert(rl1,2)
                            listaprop2.pop(rl1+1)
                    listalistas2.append(p1)
                    listalistas2.append(q1)
                    listalistas2.append(r1)

                    #Evalua las primitivas para poder meter su valor en la lista que guardara todo los resultados



                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop2:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval2.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval2.index('('), len(listaeval)-1):
                                if (listaeval2[i]=='~'):
                                    listalistas2.append(NOT (listalistas2[int (listaeval2[ i + 1])]))
                                    listaeval2.insert(i,len(listalistas2)-1)
                                    listaeval2.pop(i+1)
                                    listaeval2.pop(i+1)

                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval2.index('('), len(listaeval2)-1):

                                if(listaeval2[j]=='y'):
                                    listalistas2.append(AND(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)


                                elif(listaeval2[j]=='o'):
                                    listalistas2.append(OR(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)

                                elif(listaeval2[j]=='>'):
                                    listalistas2.append(IMPLI(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)


                                elif(listaeval2[j]=='<>'):
                                    listalistas2.append(BICO(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval2) > 1:
                        for elem2 in range(len(listaeval2)-1):
                            if(listaeval2[elem2]=='~'):
                                listalistas2.append(NOT(listalistas2[int (listaeval2[elem2+1])]))
                                listaeval2.insert(elem2,len(listalistas2)-1)
                                listaeval2.remove(listaeval2[elem2 + 1])
                                listaeval2.remove(listaeval2[elem2 + 1])
                        for elem3 in range(len(listaeval2)-1):
                            if(listaeval2[elem3]=='y'):
                                listalistas2.append(AND(listalistas2[int(listaeval2[elem3-1])] , listalistas2[int(listaeval2[elem3 + 1])]))
                                listaeval2.insert(elem3,len(listalistas2)-1)
                                listaeval2.pop(elem3-1)
                                listaeval2.pop(elem3)
                                listaeval2.pop(elem3)

                        for elem4 in range(len(listaeval2)-1):
                                if(listaeval2[elem4]=='o'):
                                    listalistas2.append(OR(listalistas2[int(listaeval2[elem4-1])] , listalistas2[int(listaeval2[elem4 + 1])]))
                                    listaeval2.insert(elem4,len(listalistas2)-1)
                                    listaeval2.pop(elem4-1)
                                    listaeval2.pop(elem4)
                                    listaeval2.pop(elem4)

                        for elem5 in range(len(listaeval2)-1):
                                if(listaeval2[elem5]=='>'):
                                    listalistas2.append(IMPLI(listalistas2[int(listaeval2[elem5-1])] , listalistas2[int(listaeval2[elem5 +1])]))
                                    listaeval2.insert(elem5,len(listalistas2)-1)
                                    listaeval2.pop(elem5 -1)
                                    listaeval2.pop(elem5)
                                    listaeval2.pop(elem5)

                        for elem6 in range(len(listaeval2)-1):
                                if(listaeval2[elem6]=='<>'):
                                    listalistas2.append(IMPLI(listalistas2[int(listaeval2[elem6-1])] , listalistas2[int(listaeval2[elem6 +1])]))
                                    listaeval2.insert(elem6,len(listalistas2)-1)
                                    listaeval2.pop(elem6 -1)
                                    listaeval2.pop(elem6)
                                    listaeval2.pop(elem6)


                else:
                    for pl in range(len(listaprop2)):
                        if listaprop2[pl]=='p':
                            listaprop2.insert(pl,0)
                            listaprop2.pop(pl+1)

                    for ql in range(len(listaprop2)):
                        if listaprop2[ql]=='q':
                            listaprop2.insert(ql,1)
                            listaprop2.pop(ql+1)
                    listalistas2.append(p)
                    listalistas2.append(q)
                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop2:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval2.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval2.index('('), len(listaeval2)-1):
                                if (listaeval2[i]=='~'):
                                    listalistas2.append(NOT (listalistas2[int(listaeval2[ i + 1])]))
                                    listaeval2.insert(i,len(listalistas2)-1)
                                    listaeval2.pop(i+1)
                                    listaeval2.pop(i+1)
                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval2.index('('), len(listaeval2)-1):

                                if(listaeval2[j]=='y'):
                                    listalistas2.append(AND(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)


                                elif(listaeval2[j]=='o'):
                                    listalistas2.append(OR(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)

                                elif(listaeval2[j]=='>'):
                                    listalistas2.append(IMPLI(listalistas2[int(listaeval2[j-1])] , listalistas2[(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)


                                elif(listaeval2[j]=='<>'):
                                    listalistas2.append(BICO(listalistas2[int(listaeval2[j-1])] , listalistas2[int(listaeval2[ j + 1])]))
                                    listaeval2.insert(j,len(listalistas2)-1)
                                    listaeval2.pop(j-1)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j)
                                    listaeval2.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval2) > 1:
                        for elem2 in range(len(listaeval2)-1):
                            if(listaeval2[elem2]=='~'):
                                listalistas2.append(NOT(listalistas2[int(listaeval2[elem2+1])]))
                                listaeval2.insert(elem2,len(listalistas2)-1)
                                listaeval2.remove(listaeval2[elem2 + 1])
                                listaeval2.remove(listaeval2[elem2 + 1])
                        for elem3 in range(len(listaeval2)-1):
                                if(listaeval2[elem3]=='y'):
                                    listalistas2.append(AND(listalistas2[int(listaeval2[elem3-1])] , listalistas2[int(listaeval2[elem3 + 1])]))
                                    listaeval2.insert(elem3,len(listalistas2)-1)
                                    listaeval2.pop(elem3-1)
                                    listaeval2.pop(elem3)
                                    listaeval2.pop(elem3)

                        for elem4 in range(len(listaeval2)-1):
                                if(listaeval2[elem4]=='o'):
                                    listalistas2.append(OR(listalistas2[int(listaeval2[elem4-1])] , listalistas2[int(listaeval2[elem4 + 1])]))
                                    listaeval2.insert(elem4,len(listalistas2)-1)
                                    listaeval2.pop(elem4-1)
                                    listaeval2.pop(elem4)
                                    listaeval2.pop(elem4)



                        for elem5 in range(len(listaeval2)-1):
                                if(listaeval2[elem5]=='>'):
                                    listalistas2.append(IMPLI(listalistas2[int(listaeval2[elem5-1])] , listalistas2[int(listaeval2[elem5 +1])]))
                                    listaeval2.insert(elem5,len(listalistas2)-1)
                                    listaeval2.pop(elem5 -1)
                                    listaeval2.pop(elem5)
                                    listaeval2.pop(elem5)

                        for elem6 in range(len(listaeval2)-1):
                                if(listaeval2[elem6]=='<>'):
                                    listalistas2.append(IMPLI(listalistas2[int(listaeval2[elem6-1])] , listalistas2[int(listaeval2[elem6 +1])]))
                                    listaeval2.insert(elem6,len(listalistas2)-1)
                                    listaeval2.pop(elem6 -1)
                                    listaeval2.pop(elem6)
                                    listaeval2.pop(elem6)
                if (listalistas[len(listalistas)-1]==listalistas2[len(listalistas2)-1]):
                    print("La proposición es equivalente\n")
                else:
                    print("La proposición no es equivalente\n")





            if contador==3:
                        #ingresa la proposición
                prop=input("ingrese su proposición:")


                p=[True,True, False, False] #Valores que pueden tomar p, q ,r y las negaciones de estás
                q=[True,False,True,False]
                t=[True,True,True,True]
                c=[False,False,False,False]

                p1=[True,True,False,False,True,True, False,False]
                q1=[True,False,True,False,True,False,True,False]
                r1=[True,True,True,True,False,False,False,False]
                t1=[True,True,True,True,True,True,True,True]
                c1=[False,False,False,False,False,False,False,False]

                #Convierte la proposición a lista
                listaprop=list(prop.split(" "))

                listaeval=[]
                listalistas=[]





                #Identifia si hay r en la proposición para saber las combinaciones de verdadero y falso necesarias
                if 'r' in listaprop:
                    for pl1 in range(len(listaprop)):
                        if listaprop[pl1]=='p':
                            listaprop.insert(pl1,0)
                            listaprop.pop(pl1+1)

                    for ql1 in range(len(listaprop)):
                        if listaprop[ql1]=='q':
                            listaprop.insert(ql1,1)
                            listaprop.pop(ql1+1)

                    for rl1 in range(len(listaprop)):
                        if listaprop[rl1]=='r':
                            listaprop.insert(rl1,2)
                            listaprop.pop(rl1+1)
                    listalistas.append(p1)
                    listalistas.append(q1)
                    listalistas.append(r1)

                    #Evalua las primitivas para poder meter su valor en la lista que guardara todo los resultados



                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval.index('('), len(listaeval)-1):
                                if (listaeval[i]=='~'):
                                    listalistas.append(NOT (listalistas[int (listaeval[ i + 1])]))
                                    listaeval.insert(i,len(listalistas)-1)
                                    listaeval.pop(i+1)
                                    listaeval.pop(i+1)

                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval.index('('), len(listaeval)-1):

                                if(listaeval[j]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)

                                elif(listaeval[j]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='<>'):
                                    listalistas.append(BICO(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval) > 1:
                        for elem2 in range(len(listaeval)-1):
                            if(listaeval[elem2]=='~'):
                                listalistas.append(NOT(listalistas[int (listaeval[elem2+1])]))
                                listaeval.insert(elem2,len(listalistas)-1)
                                listaeval.remove(listaeval[elem2 + 1])
                                listaeval.remove(listaeval[elem2 + 1])
                        for elem3 in range(len(listaeval)-1):
                            if(listaeval[elem3]=='y'):
                                listalistas.append(AND(listalistas[int(listaeval[elem3-1])] , listalistas[int(listaeval[elem3 + 1])]))
                                listaeval.insert(elem3,len(listalistas)-1)
                                listaeval.pop(elem3-1)
                                listaeval.pop(elem3)
                                listaeval.pop(elem3)

                        for elem4 in range(len(listaeval)-1):
                                if(listaeval[elem4]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[elem4-1])] , listalistas[int(listaeval[elem4 + 1])]))
                                    listaeval.insert(elem4,len(listalistas)-1)
                                    listaeval.pop(elem4-1)
                                    listaeval.pop(elem4)
                                    listaeval.pop(elem4)

                        for elem5 in range(len(listaeval)-1):
                                if(listaeval[elem5]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem5-1])] , listalistas[int(listaeval[elem5 +1])]))
                                    listaeval.insert(elem5,len(listalistas)-1)
                                    listaeval.pop(elem5 -1)
                                    listaeval.pop(elem5)
                                    listaeval.pop(elem5)

                        for elem6 in range(len(listaeval)-1):
                                if(listaeval[elem6]=='<>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem6-1])] , listalistas[int(listaeval[elem6 +1])]))
                                    listaeval.insert(elem6,len(listalistas)-1)
                                    listaeval.pop(elem6 -1)
                                    listaeval.pop(elem6)
                                    listaeval.pop(elem6)


                else:
                    for pl in range(len(listaprop)):
                        if listaprop[pl]=='p':
                            listaprop.insert(pl,0)
                            listaprop.pop(pl+1)

                    for ql in range(len(listaprop)):
                        if listaprop[ql]=='q':
                            listaprop.insert(ql,1)
                            listaprop.pop(ql+1)
                    listalistas.append(p)
                    listalistas.append(q)
                    #Evalua elemento por elemento para ver que realizar primero
                    for elem in listaprop:
                        #Agrega elementos a una lista hasta que encuentre el cierre de parentesis para poder evaluarlo
                        if(elem != ')'):
                            listaeval.append(elem)
                        if (elem == ')'):
                            #Evalua not en la proposción entre los parentesis
                            for i in range(listaeval.index('('), len(listaeval)-1):
                                if (listaeval[i]=='~'):
                                    listalistas.append(NOT (listalistas[int(listaeval[ i + 1])]))
                                    listaeval.insert(i,len(listalistas)-1)
                                    listaeval.pop(i+1)
                                    listaeval.pop(i+1)
                        if (elem == ')'):
                            #Evalua operadores logicos binarios en la proposción entre los parentesis
                            for j in range(listaeval.index('('), len(listaeval)-1):

                                if(listaeval[j]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)

                                elif(listaeval[j]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[j-1])] , listalistas[(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)


                                elif(listaeval[j]=='<>'):
                                    listalistas.append(BICO(listalistas[int(listaeval[j-1])] , listalistas[int(listaeval[ j + 1])]))
                                    listaeval.insert(j,len(listalistas)-1)
                                    listaeval.pop(j-1)
                                    listaeval.pop(j)
                                    listaeval.pop(j)
                                    listaeval.pop(j -2)
                    # Evalua la lista lista mintras tenga más elementos que 1

                    while len(listaeval) > 1:
                        for elem2 in range(len(listaeval)-1):
                            if(listaeval[elem2]=='~'):
                                listalistas.append(NOT(listalistas[int(listaeval[elem2+1])]))
                                listaeval.insert(elem2,len(listalistas)-1)
                                listaeval.remove(listaeval[elem2 + 1])
                                listaeval.remove(listaeval[elem2 + 1])
                        for elem3 in range(len(listaeval)-1):
                                if(listaeval[elem3]=='y'):
                                    listalistas.append(AND(listalistas[int(listaeval[elem3-1])] , listalistas[int(listaeval[elem3 + 1])]))
                                    listaeval.insert(elem3,len(listalistas)-1)
                                    listaeval.pop(elem3-1)
                                    listaeval.pop(elem3)
                                    listaeval.pop(elem3)

                        for elem4 in range(len(listaeval)-1):
                                if(listaeval[elem4]=='o'):
                                    listalistas.append(OR(listalistas[int(listaeval[elem4-1])] , listalistas[int(listaeval[elem4 + 1])]))
                                    listaeval.insert(elem4,len(listalistas)-1)
                                    listaeval.pop(elem4-1)
                                    listaeval.pop(elem4)
                                    listaeval.pop(elem4)



                        for elem5 in range(len(listaeval)-1):
                                if(listaeval[elem5]=='>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem5-1])] , listalistas[int(listaeval[elem5 +1])]))
                                    listaeval.insert(elem5,len(listalistas)-1)
                                    listaeval.pop(elem5 -1)
                                    listaeval.pop(elem5)
                                    listaeval.pop(elem5)

                        for elem6 in range(len(listaeval)-1):
                                if(listaeval[elem6]=='<>'):
                                    listalistas.append(IMPLI(listalistas[int(listaeval[elem6-1])] , listalistas[int(listaeval[elem6 +1])]))
                                    listaeval.insert(elem6,len(listalistas)-1)
                                    listaeval.pop(elem6 -1)
                                    listaeval.pop(elem6)
                                    listaeval.pop(elem6)
                        if (listalistas[len(listalistas)-1]==t):
                            print("La proposición es tautología")
                        if (listalistas[len(listalistas)-1]==c):
                            print("La proposición es contradicción")
                        if (listalistas[len(listalistas)-1]!=c and listalistas[len(listalistas)-1]!=t):
                            print("La proposición no es contradicción ni tautología")



            if contador==4:
                print("Bienvenido a la calculadora de proposiciones.\nPara ingresar una proposición, debes escribir todos los elementos separados\n Los simbolos de los operadores logicos son los siguiente: ~ (not) ; y (conjunción); o (disyunción); > (implicación); <> (bicondicional)\n Solo tienes permitido utilizar las proposiciones primitivas  p, q y r para evaluar.\nEjemplo: ( p y q ) > ( ~ p o r )\n")


            if contador==5:
                a=eval(input("1.Calculadora de tablas de verdad\n2.Calculadora de conjuntos\n3.Calculadora de relaciones \n4.Salir"))
