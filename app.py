#!/usr/bin/ env python3

from view import *
from controlador import *
import sys
class App:
    '''Con esta clase inicializamos el sistema'''
    @staticmethod
    def main():
        vista=view()
        try:
            control= Quiri()
        except Exception as e:
            vista.mensaje_error(e)
            exit()
        '''aca estaria faltatando poner le diccionario de opciones 
        para que una vez que el usuario elija una opcion mande al controlador'''
        opcion_producto={1: control.hacer_producto}
        opcion_compra_venta={1:control.realizar_compra_contado,2:control.realizar_venta_contado}
        while True:
            #primeramente se ejecuta el menu principal
            opcion_principal=vista.menu_principal()
            if opcion_principal==1:
                vista.clean_screen()
                opcion_producto[opcion_principal]()
                #si la opcion principal es igual a 1  ejecuta la opcion que se en
            elif opcion_principal==2:
                #si la opcion del menu principal es igual a dos se ejecuta el sub menu de movimientos
                opcion_movimiento=vista.sub_menu_movimientos()
                print(opcion_movimiento)
                if(opcion_movimiento==3):
                    #si la opcion de los movimientos es igual a 3 entonces se vuelve a ejecutar el menu pruncipal
                    continue
                opcion_compra_venta[opcion_movimiento]()
            elif opcion_principal==3:
                #si la opcion es igual a 3 se ejecuta el sub menu consultar
                opcion_consultar=vista.sub_menu_consultar()
                if(opcion_consultar==4):
                    #si la opcion_consultar es igual a cuatro se sigue ejecutando el menu principal
                    continue
                #llamamos a desplegar detalle del controlador y le pasamos la opcion
                control.desplegar_detalle(opcion_consultar)
            elif opcion_principal==4:
                #si la opcion del menu principal es igual a cuatro entonces el sistema se cierra
                sys.exit()
            else:
                pass
                
            



if __name__ == '__main__':
    App.main()
