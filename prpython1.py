numAlumnos = 5; #Número de alumnos a meter
contador = 0;
edadIntro = 0; #El número que se ha introducido en cada iteración
edadMax = 0;
edadMin = 0;
edadesPares = 0;
edadesImpares = 0;
mayorPrimo = 0;
cuentaPrimo = 0;
esPrimo = True
factorial = 1;

while contador < numAlumnos:
  edadIntro = int(input("Introduce edad: "))
  if(edadIntro > 0):
    contador += 1
    if(edadMax < edadIntro or contador == 1):
      edadMax = edadIntro
    if(edadMin > edadIntro or contador == 1):
      edadMin = edadIntro
    #El ... or contador == 1 es para comprobar si es el primer número que se introduce
    if edadIntro % 2 == 0:
      edadesPares += 1
    else:
      edadesImpares += 1

    cuentaPrimo = edadIntro - 1
    esPrimo = True
    while cuentaPrimo > 1:
      if edadIntro % cuentaPrimo == 0:
        esPrimo = False
        break
      cuentaPrimo -= 1
    if (esPrimo == True and mayorPrimo < edadIntro):
      mayorPrimo = edadIntro


print ("Edad máxima",edadMax)
print ("Edad mínima",edadMin)
print ("Edades impares",edadesImpares)
print ("Edades pares",edadesPares)

if mayorPrimo > 0:
  print("Mayor primo:",mayorPrimo)
  contador = mayorPrimo
  while contador > 0:
    factorial = factorial * contador
    contador -= 1
  print("El factorial de",mayorPrimo,"es",factorial)
else:
  print("No hay números primos")
