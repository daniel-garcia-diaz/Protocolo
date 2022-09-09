
import os

a=0
print("Bienvenido al creador de protocolos/n")

def menu():
    print('''
    Menú
    1.Crear Protocolo
    2.Añadir elemento
    3.Eliminar Protocolo
    4.Visualizar Protocolo
''')
menu()
opc=input("¿Deseas realizar una acción? s/n ")
if (opc == "N" or opc == "s" or opc == "S" or opc == "n"):

    print(" ")
    while (opc == "s" or opc == "S"):
        opcion=int(input("Escriba el número de la opción deseada "))
        
        if opcion == 1:
            print(" ")
            name=input("Escribe el nombre de tu protocolo: ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            print ('\n *Nota: Es recomendable escribir en esta opcion todas las instrucciones del protocolo ya que en la opción "Añadir" no sigue la estructura numerica')
            
            esc=input("\n ¿Deseas escribir las instruciones del protocolo? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print(" ")
                instruccion=input("Escribe la "+str(a)+"° instrucción: ")
                protocolo.write(str(a) +"-"+ instruccion + '''\n''')
                
                sub=input("Deseas escribir una sub-instruccion? s/n ")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escribe la sub-instruccion: ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("Deseas escribir la siguiente instrución? s/n ")
                print(" ")
            print("Hemos terminado el protocolo")
            print(" ")
            protocolo.close()
            
        elif  opcion == 2:
            print(" ")
            
            name=input("Escriba el nombre del protocolo al quiere agregar pasos: ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("Desea agregar una instrucion? s/n ")
            while (esc == "s" or esc=="S"):

                print(" ")
                instruccion=input("Escriba la instruccion: ")
                protocolo.write("-"+ instruccion + '''\n''')
                
                sub=input("Desea escribir una subinstruccion? s/n ")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escriba la sub-instruccion: ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("Desea escribir otra instrucion? s/n ")
                print(" ")
            print("Hemos terminado el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == 3:
            print(" ")
            name=input("Escribe el nombre del protocolo que deseas eliminar: ")
            os.remove(name + ".txt")
            print("El protocolo ha sido removido")
            print(" ")
            
        elif  opcion == 4:
            print(" ")
            name=input("Escribe el nombre del protocolo que desea visualizar: ")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()

                   
        opc=input("¿Deseas realizar otra acción? s/n ")
        if (opc=="s" or opc=="S"):
            continue
        else:
            break
    print(" ")
    print("Gracias por utilizar el programa")
    
else:
    print(" ")
    print("Gracias por utilizar el programa")
