#escribo w para escritura y r para lectura
documento = open("my_notes.txt","w") #abro el archivo my notes para su escritura
#lineas de codigo para la escritura en el archivo
documento.write(" Bernardo Antonio Vasquez Maza ")
documento.write(" Cuenca-Ecuador ")
documento.write(" 2024")
documento.close() #cierro el archivo my notes

documento = open("my_notes.txt","r") #abro el archivo my notes para su lectura
line = documento.readline() #leo la linea de codigo y almaceno en la variable line
while line: #bucle mientras haya lineas que leer, en este caso la variable line
    print(line) #imprimo el resultado de la variable line
    line=documento.readline() #leemos la siguiente linea, hasta que no hay mas cobtenido que leer

documento.close() #cierra el archivo