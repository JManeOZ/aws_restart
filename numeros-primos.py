#Almacenar los numeros primos

numeros_primos = []

for numero in range(1, 251):
    es_primo = True

    if numero == 1:
        es_primo = False

    for dividir in range (2, numero):
        if numero % dividir == 0:
            es_primo = False
        break

    if es_primo:
        numeros_primos.append(numero)
    
archivo = open("results.txt", "w")

archivo.write("Numeros primos ente el 1 y el 250")

for primo in numeros_primos:
    archivo.write(str(primo) + "\n")

archivo.close()