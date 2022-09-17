import random
import time

# Colores
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33;4m' 
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m'


puntaje = 0
record_puntaje = []

iniciar_trivia = True
intentos = 0

# Bienvenida
print ('\033[35;1m'+ "BIENVENID@ A ESTA TRIVIA SOBRE QUIMICA" + RESET)

print("Cargando trivia...")
for i in range(1,6):
  print(i)
  time.sleep(1)

# Inserta nombre
nombre = input('\nIngresa tu nombre, por favor: ' + '\033[36;47m')
print(RESET )


# Inicia loop
while iniciar_trivia == True:
  # intentos
  intentos += 1
  
  # Asigna puntaje
  puntaje = random.randint(0, 10)

  # Instrucciones
  print (GREEN + "Hola, ", nombre,
         ".Este es tu intento número ", intentos, ".\n\nTus conocimientos básicos en química se pondrán a prueba." + RESET, end='')
  
  time.sleep(2)
  
  print('\nPero antes, veamos cuánta suerte tienes.')
  
  time.sleep(1)
  
  input('\033[32;47m' + '\n(Presiona ENTER para ver cuántos puntos de regalo tienes)' + RESET)
  
  
  if puntaje == 0:
    print(':( obtuviste un puntaje de', 
          str(puntaje),
          '\n¡Pero nada mejor que confiar en tus conocimientos para poder alcanzar un buen puntaje!')
  elif(puntaje == 1) :
    print(':) Tu suerte te ha hecho ganar',
          str(puntaje),
          'punto.\nAhora veamos lo que puedes ganar con tus conocimientos.')
  else:
    print(':D Tu suerte te ha hecho ganar',
          str(puntaje),
          'puntos.\nAhora veamos lo que puedes ganar con tus conocimientos.')
  
  input('\033[32;47m' + '\n(Presiona ENTER)' + RESET)
  
  
  # Instrucciones
  print (YELLOW + "\nResponde solo la letra de la alternativa y presiona \n'ENTER' para enviar tu respuesta." + RESET)

  time.sleep(1.5)
      
  print(YELLOW + "\nCon cada respuesta correcta ganas 10 puntos.\nY por cada error se descuenta un puntaje aleatorio entre 1 y 10" + RESET )
  time.sleep(2)
  input('\033[32;47m' + '\nListos para empezar? (presiona ENTER cuando estes list@)' + RESET)


  print("\nCargando preguntas...")
  for i in range(1,4):
    print(i)
    time.sleep(1)

  
  # Pregunta 1
  print(BLUE)
  print ("\n1) ¿Qué elemento químico (metal) es líquido a condiciones ambientales?")
  print ("a) Bromo")
  print ("b) Galio")
  print ("c) Mercurio")
  print ("d) Germanio" + RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  rpta_1 = input('\nRespuesta: ')
  
  while rpta_1 not in ('a','b','c','d','q'):
    rpta_1 = input('\nDebes responder a, b, c o d. \n(existe una letra diferente a estas que \nte puede dar un mensaje secreto): ')
  
  if rpta_1 == 'q':
    print('\nAcabas de encontrar un mensaje secreto. \nPrimera palabra: UN.')
    rpta_1 = input('\nAhora elige tu respuesta: ')
  
  while rpta_1 not in ('a', 'b', 'c', 'd'):
    rpta_1 = input('\nElige una alternativa entre a, b, c o d: ')
    
  if rpta_1 == 'c':
    print('\nCorrecto!')
    gana = 10
    puntaje += gana
    print('\nHaz ganado', gana, 'puntos')
  elif rpta_1 == 'a':
    print('\nOops ese elemento sí es líquido a temperatura de ambiente pero es un no metal.')
    pierde = random.randint(1,10)
    puntaje -= pierde
    print('\n:(  Haz perdido', pierde, 'puntos')
  else:
    print('\nParece que ese elemento no es líquido a temperatura de ambiente')
    pierde = random.randint(1,10)
    puntaje -= pierde
    print('\n:(  Haz perdido', pierde, 'puntos')

  time.sleep(3)
  print(MAGENTA + "\nTienes hasta ahora ", puntaje, " puntos.\n" + RESET, end = "")

  time.sleep(2)


  
  # Pregunta 2
  print("\nLa siguietne pregunta duplicará tu puntaje si es correcto\nO lo reducirá a la mitad si es totalmente incorrecto.")
  print(BLUE)
  print ("\n2) ¿Qué compuesto químico es el principal causante del calentamiento global?")
  print ("a) Dióxido de carbono(CO2)")
  print ("b) Metano (CH4)")
  print ("c) Ozono (O3)")
  print ("d) Kriptonita (Kr)" + RESET)
  
  # Almacenamos la respuesta del usuario en la variable "respuesta_1"
  rpta = input('\nRespuesta: ')
  
  while rpta not in ('a','b','c','d','r'):
    rpta = input('\nDebes responder a, b, c o d. \n(existe una letra diferente a estas que \nte puede dar un mensaje secreto): ')
  
  if rpta == 'r':
    print('\nAcabas de encontrar un mensaje secreto. \nSegunda palabra: NUEVO.')
    rpta = input('\nAhora elige tu respuesta: ')
  
  while rpta not in ('a', 'b', 'c', 'd'):
    rpta = input('\nElige una alternativa entre a, b, c o d: ')
    
  if rpta == 'a':
    print('\nCorrecto!')
    puntaje *= 2
    print('\nTu puntaje se ha duplicado!')
  elif rpta == 'b':
    print('\nEse elemento sí ocasiona calentamiento global, mas no es el principal causante.')
    gana = 5
    puntaje += gana
    print('\n:(  Haz ganado', gana, 'puntos')
  elif rpta == 'c':
    print('\nEste elemento está implicado con la capa de ozono')
    pierde = 5
    puntaje -= pierde
    print('\n:(  Haz perdido', pierde, 'puntos')
  else:
    print("\nEsto es algo loco! La kirptonita sólo existe en Superman.")
    puntaje /= 2
    print("\nTu puntaje se ha reducido a la mitad :(")
  time.sleep(1)
  print("\nAhora tienes", puntaje, "puntos")

  time.sleep(2)


        
  # Pregunta 3
  alternativas = ["a) Derretimiento del hielo",
                  "b) Disolución de la sal en agua",
                  "c) Combustión del GNV",
                  "d) evaporación del agua"]
  print("\nEsta pregunta te dará puntajes aleatorios. Suerte!")
  print(GREEN)
  time.sleep(2)
  print('Cuál de las siguientes alternativas representa un cambio químico?')
  time.sleep(1.5)
  for alternativa in alternativas:
    print(alternativa)
    time.sleep(1)
  print ( RESET)

  # Almancenar rpta
  rpta = input('\nRespuesta: ')

  # Recibir sólo alternativas y alternativa secreta:
  while rpta not in ('a','b','c','d','s'):
    rpta = input('\nDebes responder a, b, c o d. \n(existe una letra diferente a estas que \nte puede dar un mensaje secreto): ')

  # Mensaje si descubre alternativa secreta
  if rpta == 's':
    print('\nAcabas de encontrar un mensaje secreto. \nTercera palabra: FUTURO.')
    time.sleep(1)
    print('\nFelicidades! Lograste armar la frase: Un nuevo futuro.')
    time.sleep(2)
    print('\nPor ello te daremos 200 puntos! :D')
    time.sleep(1)
    puntaje += 200
    print("\nAhora tienes:", puntaje, "puntos.")
    time.sleep(1)
    rpta = input('\nAhora elige tu respuesta: ')

  # Escogiendo alternativas reales
  while rpta not in ('a', 'b', 'c', 'd'):
    rpta = input('\nElige una alternativa entre a, b, c o d: ')

  # Condicional para asignar puntaje
  if rpta == 'a':
    print('\nEl derretimiento del hielo es un cambio físico. :(')
    pierde = random.randint(2,10)
    puntaje -= pierde
    print('\nPierdes', pierde, "puntos")
  elif rpta == 'b':
    print('\nLa disolución de sal en agua no implica ninguna reacción química por lo que es un cambio físico.')
    pierde = random.randint(2,10)
    puntaje -= pierde
    print('\n:( Pierdes', pierde, 'puntos')
  elif rpta == 'c':
    print('\nCorrecto! el proceso de combustión de cualquier material es un cambio químico')
    gana = random.randint(2,10)
    puntaje += gana
    print('\n:D  Haz ganado', gana, 'puntos')
  else:
    print("\nLa evaporación del agua es un cambio físico :(")
    pierde = random.randint(2,10)
    puntaje -= pierde
    print("\nHaz perdido", pierde, "puntos.")
  time.sleep(1)
  print(GREEN + "\nAhora tienes", puntaje, "puntos acumulados."+RESET)
  time.sleep(2)

  print("\n",nombre, ", hemos llegado al final de la trivia.")
  time.sleep(2)

  record_puntaje.append(puntaje)
  print("\nHasta ahora estos fueron tus puntajes:")
  
  for puntaje in record_puntaje:
    print(MAGENTA + str(puntaje) + RESET)
  time.sleep(1)
  print("\nEl mayor puntaje fue", max(record_puntaje))
  time.sleep(1.5)
  print("La suma de tu puntaje final en todos los intentos es", sum(record_puntaje))
  time.sleep(2)
  print("\n¿Deseas intentar la trivia nuevamente y ver cómo te va esta vez?")
  time.sleep(2)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para temrinar: ").lower()

  if repetir_trivia != "si":
   print("\nEspero que la hayas pasado súper respondiendo esta pequeña trivia,", nombre, ", hasta pronto!")
   iniciar_trivia = False 
