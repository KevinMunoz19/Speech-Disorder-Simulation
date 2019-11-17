#Julio Merida
#Kevin Munoz

#Importar libreria pyttsx3 y random
import pyttsx3 as tts
import random

#Seleccionar el tipo de tartamudez
#0 agrega la repeticion de una palabra
#1 agrega un sonido de pausa 'um'
stutter_type=1

array = []

with  open("textfile.txt", "r") as f:           #Abrir el archivo txt con el nombre textfile y guardar cada linea del archivo en una posicion del array
    array = f.read().splitlines()

lengthArray = len(array)            #Obtener el tamano del array
lengthArray=lengthArray - 1

i=0
#Leer la pisicion del array, separar por palabras la oracion, de manera aleatoria seleccionar una palabra y agregarla
#a la oracion 
while i <= lengthArray:
    line = array[i]
    line = line.split()
    
    length = len(line)
    length=length-1
    random_number = random.randint(0,length)
    if stutter_type == 0:
        added_string=line[random_number]
    if stutter_type == 1:
        added_string="um"
    line.insert(random_number,added_string)
    array[i]=line
    i=i+1


print(array)    #Mostrar el array

engine = tts.init()
rate = engine.getProperty('rate')   
engine.setProperty('rate', 200)     #set del rate de habla
engine.say(array)                   
engine.runAndWait()

f.close()                   #Cerrar el archivo txt 
