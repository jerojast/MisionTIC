print("Este programa verifica si los últimos dígitos son iguales")

print("Inicio del programa")

print("Escriba dos números enteros: ")

num1=int(input())

num2=int(input())

if num1<0:
    num1=num1*(-1)

elif num2<0:
        
    num2=num2*(-1)

ud1=num1-num1//(10*10)
ud2=num2-num2//(10*10)

elif ud1==ud2:
    print("El último dígito de un número es igual al del otro")

else:
    print("El último dígito de un número no es igual al del otro")
