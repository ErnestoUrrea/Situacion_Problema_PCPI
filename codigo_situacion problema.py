#IMPORTS
import matplotlib.pyplot as plot
import csv
import math
#FIN IMPORTS

#DEFINICION DE FUNCIONES

# Funcion para transponer una lista
def Transponer(lista): #Nota, se debe recibir una lista, no vacia, con el mismo numero de elementos en cada fila
    transpuesta = []
    
    filas = len(lista)
    columnas = len(lista[0])

    for numcolumna in range(columnas):
        transpuesta.append([])
        for numfila in range(filas):
            transpuesta[numcolumna].append(lista[numfila][numcolumna])

    return transpuesta

#FIN DEFINICION DE FUNCIONES

#Importamos el archivo
nombreArchivo = 'NYC Accidents 2020.csv'
with open(nombreArchivo, newline = '') as archivo:
    datos = csv.reader(archivo)
    lista = list(datos)
    
#Transponemos el arreglo de datos
listaDatos = Transponer(lista)
titulos = []

for fila in listaDatos:
    titulos.append(fila[0])
    fila.pop(0)

#for fila in listaDatos:
#    print(titulos[listaDatos.index(fila)], fila[0])

#Convertimos la fecha de string de la forma 'AAAA-MM-DD' a una lista de la forma [AAAA, MM, DD].
fechas = [] #En formato [Anio, Mes, Dia]
meses = []
for strFecha in listaDatos[titulos.index('CRASH DATE')]:
    splitStrFecha = strFecha.split('-')
    fecha = [int(splitStrFecha[0]), int(splitStrFecha[1]), int(splitStrFecha[2])]
    meses.append(int(splitStrFecha[1]))
    fechas.append(fecha)

#Convertimos la hora de string de la forma '00:00:00' a un float de la hora correspondiente.
horaDelDia = [] #En horas
for strHora in listaDatos[titulos.index('CRASH TIME')]:
    splitStrHora = strHora.split(':')
    #hora = [int(splitStrHora[0]), int(splitStrHora[1]), int(splitStrHora[2])]
    hora = int(splitStrHora[0]) + int(splitStrHora[1])/60 + int(splitStrHora[2])/3600
    horaDelDia.append(hora)

#Graficamos los meses en los que mas se producen accidentes
intervalosAnios = range(math.ceil(min(anios)), math.ceil(max(anios))+1) #calculamos los extremos de los intervalos
plot.hist(x=anios, bins=intervalosAnios, color='#F2AB6D', rwidth=0.85)
plot.title('Grafica de anio del accidente por frecuencias')
plot.xlabel('Anio')
plot.ylabel('Frecuencia')
plot.xticks(intervalosAnios)
plot.show() #Mostramos el histograma

#Graficamos la fecha del mes con mas accidentes en que mas se producen accidentes
intervalosMes = range(math.ceil(min(meses)), math.ceil(max(meses))+1) #calculamos los extremos de los intervalos
plot.hist(x=meses, bins=intervalosMes, color='#F2AB6D', rwidth=0.85)
plot.title('Grafica de mes del accidente por frecuencias')
plot.xlabel('Meses')
plot.ylabel('Frecuencia')
plot.xticks(intervalosMes)
plot.show() #Mostramos el histograma

#Graficamos las horas del dia
intervalosHora = range(math.ceil(min(horaDelDia)), math.ceil(max(horaDelDia))+1) #calculamos los extremos de los intervalos
plot.hist(x=horaDelDia, bins=intervalosHora, color='#F2AB6D', rwidth=0.85)
plot.title('Grafica de hora del accidente por frecuencias')
plot.xlabel('Hora')
plot.ylabel('Frecuencia')
plot.xticks(intervalosHora)
plot.show() #Mostramos el histograma

print(fechas[0])
print(anios)
print(meses[0])
print(horaDelDia[0])


        
        
