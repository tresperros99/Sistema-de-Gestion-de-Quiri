import os

class view:
    '''Clase encargada de mostrar los menus al usuario, tambien
    de mandar mensajes  y de recibir los datos necesarios para 
    el funcionamiento del sistema'''
    def menu_principal(self):
        '''metodo que se encarga de mostrar el menu principal 
        al usuario'''
        opcion=-1
        while opcion<1 or opcion>4:
            view.clean_screen(self)
            print('-------------------------------------------')
            print('Bienvenido al sistema de Gestion de Quiri')
            print('-------------------------------------------')
            print('\t\tMenu principal')
            print('1- Cargar Productos')
            print('2- Realizar Movimientos')
            print('3- Consultar')
            print('4- Salir')
            opcion=view.leer_numero(self)
        return opcion
    
    def sub_menu_movimientos(self):
        opcion=-1
        while opcion<1 or opcion>3:
            view.clean_screen(self)
            print('-------------------------------------------')
            print('\t\tMovimientos')
            print('1- Movimientos de Compra')
            print('2- Movimientos de Venta')
            print('3- Salir')
            opcion=view.leer_numero(self)
        return opcion
    def sub_menu_consultar(self):
        opcion=-1
        while opcion<1 or opcion>4:
            view.clean_screen(self)
            print('-------------------------------------------')
            print('\t\t Consultar')
            print('1- Movimientos de Compra')
            print('2- Movimientos de Venta')
            print('3- Todos los Movimientos')
            print('4- Salir')
            opcion=view.leer_numero(self)
        return opcion

    def clean_screen(self):
        os.system('clear')

    def leer_numero(self):
        '''Metodo que sirve para leer numeros y validad 
        que efectivamente sea un numero'''
        while True:
            try:
                opcion=int(input())
                return opcion
            except ValueError:
                print('Usted no a ingresado un numero')
    
    def cargar_cantidad_producto(self): 
        '''metodo que sirve para cargar el producto y retornarle al controlador'''
        while True:
            try:
                cantidad= int(input("Ingrese la cantidad porfavor: "))
                assert cantidad>0
                return cantidad
            except AssertionError:
                print("no se permiten numeros negativos")
            except ValueError:
                print('Ingrese un numero valido porfavor')
    
    def cargar_tipo_producto(self):
        '''metodo que sirve para cargar el tipo de producto y retornarle al controlador'''
        tipo="x"
        while tipo!='SUPERMATE' and tipo!='MATEDULCE' and tipo!='SALIR':
            if tipo=='SALIR':
                return tipo
            tipo=input("Ingrese el tipo de producto porfavor \n(ingrese salir si desea volver al menu principal) \n SUPERMATE O MATEDULCE:\n")
            tipo=tipo.upper()
        return tipo
    
    def cargar_tipo_insumo(self):
        '''metodo que sirve para cargar el tipo de insumo y retornarle al controlador'''
        while True:
            try:
                tipo=input("Ingrese el tipo de insumo  a comprar porfavor:")
                if tipo.isalpha():
                    tipo=tipo.lower()
                    return tipo
                else:
                    #en el caso de que haya numeros en el tipo, entonces se levanta la excepcion
                    raise TypeError
            except TypeError:
                print("usted no a ingresado un nombre valido")
                continue

            

    def cargar_cantidad_insumo(self):
        '''metodo que sirve para cargar la cantidad de insumos y retornarle al controlador'''
        while True:
            try:
                cantidad=int(input("Ingrese la cantidad de Insumos porfavor: "))
                #en el caso que no se introduzcan solo numero se levanta la excepcion
                #validamos que la cantidad sea mayor a 0
                assert cantidad>0
                return cantidad
            except AssertionError:
                print("no se permite numeros negativos")
            except ValueError:
                print("Usted no a ingresado un numero valido")
                continue
    
    def cargar_precio_insumo(self):
        '''Metodo que sirve para cargar el precio del insumo y retornarle al controlador'''
        precio=0
        while True:
            try:
                precio=int(input("Ingrese el precio del Insumo porfavor: "))
                assert precio>0 #validamos que el precio sea mayor a 0
                return precio
            except AssertionError:
                print("precio invalido")
            except ValueError:
                print("Ingrese un numero porfavor")

    def cargar_precio_producto(self):
        '''Metodo que sirve para cargar el precio del insumo y retornarle al controlador'''
        precio=0
        while True:
            try:
                precio=int(input("Ingrese el precio del Producto porfavor: "))
                assert precio>0 #validamos que el precio sea mayor a 0
                return precio
            except AssertionError:
                print("precio invalido")    
    def confirmar_creacion_producto(self):
        '''Con este metodo confirmamos la creacion del producto
        si ponemos si se confirma y no se pone N se vuelve al menu cargar producto'''
        os.system('clear')
        r='X'
        while r!='NO' and r!='SI':
            r = input('Desea crear el producto ingrese "SI" o "NO"')
            r= r.upper()
        if r=='si':
            return True
        else: 
            return False
    def desplegar_movimientos_de_compra(self,lista):
        '''En el caso que queramos ver solo movimientos de compras filtramos por compra'''
        print('{:^20}{:^50}{:^27}{:^16}'.format('Producto', 'Cantidad', 'Precio','Fecha'))
        print('{:^20}[{:^50}][{:^20}][{:^20}]'.format('--------------------', '--------------------------------------------------', '--------------------','--------------------'))
        for x in range(len(lista)):
            if lista[x].tipo_movimiento=='compra':
                print('{:^20}[{:^50}][{:^20}][{:^20}]'.format(str(lista[x].detalle_movimiento[1]), str(lista[x].detalle_movimiento[2]), str(lista[x].detalle_movimiento[3]), str(lista[x].detalle_movimiento[4])))

    def desplegar_movimientos_de_venta(self,lista):
        '''En el caso que queramos ver solo movimientos de compras filtramos por venta'''
        print('{:^20}{:^50}{:^27}{:^16}'.format('Producto', 'Cantidad', 'Precio','Fecha'))
        print('{:^20}[{:^50}][{:^20}][{:^20}]'.format('--------------------', '--------------------------------------------------', '--------------------','--------------------'))
        for x in range(len(lista)):
            if lista[x].tipo_movimiento=='venta':
                print('{:^20}[{:^50}][{:^20}][{:^20}]'.format(str(lista[x].detalle_movimiento[1]), str(lista[x].detalle_movimiento[2]), str(lista[x].detalle_movimiento[3]), str(lista[x].detalle_movimiento[4])))
    def desplegar_movimientos(self,lista):
        '''En el caso que queramos ver solo movimientos '''
        print('{:^20}{:^50}{:^27}{:^16}'.format('Producto', 'Cantidad', 'Precio','Fecha'))
        print('{:^20}[{:^50}][{:^20}][{:^20}]'.format('--------------------', '--------------------------------------------------', '--------------------','--------------------'))
        for x in range(len(lista)):
            print('{:^20}[{:^50}][{:^20}][{:^20}]'.format(str(lista[x].detalle_movimiento[1]), str(lista[x].detalle_movimiento[2]), str(lista[x].detalle_movimiento[3]), str(lista[x].detalle_movimiento[4])))

            # print(,,,)

    def imprimir_mensaje_error_producto(self,descripcion):
        '''con este metodo imprimimos cualquier mensaje de error generico'''
        print("Lo siento el stock de insumo "+descripcion+" no es suficiente para crear el producto ")
    def imprimir_mensaje_exito(self):
        '''con este metodo imprimimos cualqueir mensaje de exito generico'''
        print("Procesado con exito!!!") 
    def imprimir_producto_no_creado(self):
        '''con este metodo indicamos que el producto no se pudo crear'''
        print("LO SIENTO EL PRODUCTO NO SE PUDO CREAR")
    def imprimir_producto_creado(self):
        '''con este metedo indicamos que el producto se pudo crear'''
        print("EL PRODUCTO FUE CREADO CON EXITO")

    def generar_pausa(self):
        ''' metodo que sirve para generar una pauasa en el programa, el usario debe ingresar enter para continuar'''
        input("Ingrese enter para continuar")
        self.clean_screen()
    def error_vender_producto(self):
        '''metodo que sirve para mostrar un error en caso de que no se pueda generar un producto'''
        print("No existe Produtos suficientes para vender")

    def mensaje_error(self, error):
        print(error)
