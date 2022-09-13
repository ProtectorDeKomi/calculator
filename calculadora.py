def main():
    print("Suma : +\nResta : -\nMultiplicacion : x\nDivicion : /\nPorcentaje : %\nPotencia : **\n\n")
    val1 = int(input("Valor Primario :"))
    var = input("Operacion :")
    val2 = int(input("Valor secundario :"))
    
    if "x" in var:
        echo = val1 * val2
        print(echo)
    else:
        if "+" in var:
            echo = val1 + val2
            print(echo)
        else:
            if "-" in var:
                echo = val1 - val2
                print(echo)
            else:
                if "/" in var:
                  echo = val1 // val2
                  print(echo)  
                else:
                    if "**" in var:
                        echo = val1 ** val2
                        print(echo) 


        
main()
