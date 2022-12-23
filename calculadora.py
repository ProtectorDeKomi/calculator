import sys

def manual():
    """"
    Calculadora En Terminal
    Ejemplo De Uso:
    
    Suma
    Valor Primario : 1
    Operacion : +
    Valor Secundario : 3

    Resta
    Valor Primario : 6
    Operacion : -
    Valor Secundario : 2

    Multiplicacion
    Valor Primario : 10
    Operacion : x
    Valor Secundario : 4

    Divicion
    Valor Primario : 1
    Operacion : /
    Valor Secundario : 3

    Porcentaje
    Valor Primario : 10
    Operacion : %
    Valor Secundario : 3

    Potencias
    Valor Primario : 1
    Operacion : **
    Valor Secundario : 3
    """
    help.__doc__

def brain(num1,oper,num2):

    operation = ['+', '-', 'x','/','*','%']
    if oper in operation:
        if oper == '+':
            print(num1 + num2)
        elif oper == '-':
            print(num1 - num2)
        elif oper == 'x':
            print(num1 * num2)
        elif oper == '/':
            print(num1 / num2)
        elif oper == '%':
            print(num1 % num2)

    else:
        print(f"La Opcion '{oper}' No Es Valida")

if __name__ == "__main__":
    option = int(input("""
    Calculadora Basica En Terminal By Astartes

    1) Usar Calculadora
    2) Ayuda
    3) Salir

    Opcion : """))
    if option == 3:
        sys.exit()
    elif option == 1:
        val1 = float(input("Valor Primario :"))
        var = input("Operacion :")
        val2 = float(input("Valor secundario :"))
        brain(val1, var,val2)
    elif option == 2:
        help(manual)
