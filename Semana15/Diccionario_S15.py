informacion_personal = {"Nombre":"Brandon","Edad":22,"Ciudad":"Cuenca","Profesion":"Ingeniero"}#creacion del diccionario
print(f"Diccionario sin modificacion {informacion_personal}")
informacion_personal["Ciudad"]="Guayaquil"#agrego ciudad
print(f"Cambio de ciudad:{informacion_personal}")
informacion_personal["Salario"]=1200#agrego salario refente a la profesion
print(f"Agrego salario: {informacion_personal}")
informacion_personal["Telefono"]=987654321#agrego telefono
print(f"Agrego Telefono: {informacion_personal}")
del(informacion_personal["Edad"])#elimino edad
print(f"Elimino edad: {informacion_personal}")
