from  view import *
from datetime import *
from model import *
from Modulos.clases import *
from abc import ABCMeta, abstractmethod
from datetime import datetime

class Empresa(metaclass=ABCMeta):
	'''Generalizacion del modelo de negocios'''

	def __init__(self,nombre):
		self.nombre=nombre


class Quiri (Empresa):
	def __init__(self):
		#Instanciamos la clase padre
		Empresa.__init__(self,'Quiri')
		self.vista=view()
		self.modelo=Model()
		try:
			self.productos = self.modelo.obtener_datos('productos')
			self.insumos = self.modelo.obtener_datos('insumos')
			self.movimientos = self.modelo.obtener_datos('movimientos')
		except Exception as e:
			raise e
	def hacer_producto(self):
		'''Metodo encargado para manufacturar los productos'''
		cantidad_producto=0
		
		confirmar=True
		while confirmar:
			'''Primeramente le pedimos al usuario que nos inserte la cantidad y el tipo de producto'''
			tipo_producto=self.vista.cargar_tipo_producto()
			if tipo_producto=='SALIR':
				break
			# self.vista.confirmar_creacion_producto()
			cantidad_producto=self.vista.cargar_cantidad_producto()
			if tipo_producto=="SUPERMATE":
				#si es que el tipo de producto es igual a supermate entonces generamos la receta para supermate
				receta_supermate=['naranja','anis','siemprevive','manzanilla','burrito','eneldo']
				self.comprobar_existencia_y_crear(receta_supermate, cantidad_producto)
			elif tipo_producto=="MATEDULCE":
				#si es que el tipo de producto es igual a matedulce entonces generamos la receta para matedulce
				receta_matedulce=['naranja','anis','cocorallado']
				self.comprobar_existencia_y_crear(receta_matedulce,cantidad_producto)

	
	def comprobar_existencia_y_crear(self,ingredientes,cantidad):
		'''Este metodo va a comprobar con la lista de ingredientes y la cantidad si 
		existen insumos disponibles para la creacion de productos'''
		# naranja=Insumo(150,20000,'naranja')
		# anis=Insumo(150,15000,'anis')
		# cocorallado=Insumo(150,3000,'cocorallado')
		# objeto3=Insumo(300,3000)
		lista_insumos=[]
		lista_insumos=self.insumos
		#cramos una lista donde vamosa almazenar todos los retornos, (TRUE OR FALSE)
		lista_verificadora=[]
		
		for x in ingredientes:
			for y in range(len(lista_insumos)):
			#creamos dos cilos anidados para poder comparar la lista de insumos, con los ingredientes
				if x==lista_insumos[y].descripcion:
					#si es que el nombre del ingrediente y la descripcion del objeto de tipo ingrediente coinciden
					#entonces se procede la llamada al metodo restar insumo
					retorno=lista_insumos[y].verificar_existencia(cantidad)
					#se añade a la lista retorno para su despues verificacion
					lista_verificadora.append(retorno)	
					if(retorno==False):
						#se imprime que insumo falta en el stock
						self.vista.imprimir_mensaje_error_producto(lista_insumos[y].descripcion)
		#si existe algun false en la lista verificadora, entonces se procede a llamada del metodo de vista
		#producto no creado. En caso contrario, se procede a la llamada del metodo de vista, producto creado
		if(False in lista_verificadora):
			self.vista.imprimir_producto_no_creado()
			self.vista.generar_pausa()			
		else:
			for z in ingredientes:
				for u in range(len(lista_insumos)):
					if z==lista_insumos[u].descripcion:
						lista_insumos[u].restar_insumo(cantidad)
			self.vista.imprimir_producto_creado()
		for u in range(len(self.productos)):
			if self.productos[u].tipo_producto=="MATEDULCE":
				self.productos[u].cantidad+=cantidad
			elif self.productos[u].tipo_producto=="SUPERMATE":
				self.productos[u].cantidad+=cantidad
		self.modelo.cargar_datos(self.productos,'productos')
		self.modelo.cargar_datos(self.insumos,'insumos')
			

	def realizar_compra_contado(self):
		'''Este metodo esta encargado de realizar las compras de insumos al contado
		'''

		confirmar=True
		while confirmar:
			self.vista.clean_screen()
			#primeramente pedimos el tipo de insumo a comprar
			tipo_insumo=self.vista.cargar_tipo_insumo()
			#luego pedimos la cantidad de insumo a comprar
			cantidad_insumo=self.vista.cargar_cantidad_insumo()
			#por ulitmo el precio del insumo a comprar
			precio_insumo=self.vista.cargar_precio_insumo()
			confirmar=False

			#creamos un ciclo para recorrer el vector de insumos
			#buscamos primeramente si ya existe el insumo, si el insumo ya exista, solo se suma la cantidad en otro caso se añade uno nuevo
			retorno=False
			for x in range(len(self.insumos)):
				if tipo_insumo== self.insumos[x].descripcion:
					retorno=self.insumos[x].sumar_insumo(cantidad_insumo)
					if retorno==True:
						self.vista.imprimir_mensaje_exito()
						break
			if retorno==False:
				#en el caso en el que retorno sea igual a false entonces añadimos un nuevo insumo a la lista 
				insu=Insumo(cantidad_insumo,precio_insumo,tipo_insumo)
				self.insumos.append(insu)
				self.vista.imprimir_mensaje_exito()
			self.vista.generar_pausa()
			#una vez cargado el nuevo producto procedemos a crear la instancia de compra contado
			#obtenemos la fecha de hoy
			fecha_hoy=datetime.now()
			fecha_hoy=fecha_hoy.date()
			#creamos la instancia del movimiento de compra Contado
			compra=CompraContado(precio_insumo,cantidad_insumo,0,{},fecha_hoy)
			compra.generar_detalle(tipo_insumo)			
			#añadimos a la lista de movimientos
			self.movimientos.append(compra)
			#añadimos a la base de datos
			self.modelo.cargar_datos(self.movimientos,"movimientos")
			self.modelo.cargar_datos(self.insumos,'insumos')

		
	
	def realizar_venta_contado(self):
		'''Este metodo esta encargado de realizar las ventas al contado'''
		confirmar=True
		while confirmar:
			self.vista.clean_screen()
			#primeramente pedimos el producto a vender
			nombre_producto=self.vista.cargar_tipo_producto()
			if nombre_producto=='SALIR':
				#si al nombre del producto recibe salir, se vuelve al menu principal
				break
			#luego pedimos la cantidad a vender
			cantidad_a_vender=self.vista.cargar_cantidad_producto()
			#por ultimo el precio del producto
			#precio_producto=self.vista.cargar_precio_producto()		
			#creamos un ciclo para recorrer el vector de productos
			#comprobamos que exista la cantidad de producto a vender 
			#si no existe mostraremos un mensaje si existe se vendera el producto
			bandera=0
			for x in range(len(self.productos)):
				if self.productos[x].tipo_producto==nombre_producto:
					retorno=self.productos[x].restar_cantidad(cantidad_a_vender)
					if retorno==True:
						self.vista.imprimir_mensaje_exito()
						bandera=x
						break
			if retorno==False:
				self.vista.error_vender_producto()
			input()
			#una vez que se resto del stock los productos se procede a realizar el movimiento
			fecha_hoy = datetime.now()
			fecha_hoy = fecha_hoy.date()
			#creamos la instancia del movimiento de venta Contado
			venta=VentaContado(self.productos[bandera].precio,cantidad_a_vender,0,{},fecha_hoy)
			#añadimos a la lista de moviemientos
			venta.generar_detalle(nombre_producto)
			self.movimientos.append(venta)
			#añadimos en la base de datos

			self.modelo.cargar_datos(self.productos,'productos')
			self.modelo.cargar_datos(self.movimientos,'movimientos')

	def desplegar_detalle(self,parametro):
		'''Con este metodo nos dispondremos a desplegar los detalles del movimiento en pantalla
		para que el usuario pueda ver recibe un parametro para poder filtrar el despliegue'''
		if(parametro==1):
			self.vista.desplegar_movimientos_de_compra(self.movimientos)
			self.vista.generar_pausa()
		elif(parametro==2):
			self.vista.desplegar_movimientos_de_venta(self.movimientos)
			self.vista.generar_pausa()
		elif(parametro==3):
			self.vista.desplegar_movimientos(self.movimientos)
			self.vista.generar_pausa()
	
	
