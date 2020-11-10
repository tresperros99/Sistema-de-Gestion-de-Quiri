import pickle
ARCHIVO_PRODUCTOS='Persistencia/productos.pickle'
ARCHIVO_INSUMOS='Persistencia/insumos.pickle'
ARCHIVO_MOVIMIENTOS='Persistencia/movimientos.pickle'
diccionario={'productos' : ARCHIVO_PRODUCTOS ,'insumos': ARCHIVO_INSUMOS,'movimientos':ARCHIVO_MOVIMIENTOS }
class Model:
	'''Clase encargarda de realizar la persistencia de objeto usando pickle
	para su posterior uso en el programa
	'''
    def cargar_datos(self, lista,directorio):
        file = open(diccionario[directorio], "wb")
        pickle.dump(lista, file)
        file.close()


    def obtener_datos(self,directorio):
        try:
            file = open(diccionario[directorio], "rb")
            temp = pickle.load(file)
        except FileNotFoundError as e:
            raise Exception("archivo no encontrado")
        except EOFError as e:
            raise Exception("Error en la base de datos")
        file.close()
        return temp 

# test=Model()
# lista=[]
# test.cargar_datos(lista,'movimientos')
# test2=test.obtener_datos_empleados()
# print(test2)
