#funcion descuento monto total del 10%
def calcular_descuento(monto_total, procentaje_descuento=10):
    descuento= monto_total*(procentaje_descuento/100)
    return descuento


monto1= 1000 #defino valor total
montototal1=calcular_descuento(monto1)#1ra llamada de la funcion
monto_final1=monto1 #resultado valor total final

print(f"Monto total: ${monto_final1}")

porcentaje_descuento2 = 10 #defino porcentaje de descuento
descuento2= calcular_descuento(monto1,porcentaje_descuento2)#2da llamada de la funcion
monto_final2 = monto1 - descuento2

print(f"Monto total: ${monto1}, Descuento: ${descuento2}({porcentaje_descuento2}%), Monto final a pagar: ${monto_final2}")
