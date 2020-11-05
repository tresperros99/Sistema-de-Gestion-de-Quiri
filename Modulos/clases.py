class Producto :
	'''Esta clase sirve para materializar los productos a travez de la mezcla de productos , para poder empaquetar.'''
	def __init__(self,tipo_producto,cantidad,precio=0) : 
		self.tipo_producto = tipo_producto # 
		self.cantidad = cantidad #
		self.precio = precio
		self.asignar_precio()
	def asignar_precio (self) :
		if self.tipo_producto=='MATEDULCE':
			self.precio=5000
		else:
			self.precio=10000
	def restar_cantidad(self,cantidad_a_restar):
		if cantidad_a_restar<=self.cantidad:
			self.cantidad=self.cantidad-cantidad_a_restar
			return True
		else:
			return False

	
class Movimiento :
	'''Clase para gestionar los movimientos de la empresa es una clase abstracta'''
	def __init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha) :
		self.importe = importe # 
		self.cantidad_productos =cantidad_productos # 
		self.total_movimiento = total_movimiento # 
		self.detalle_movimiento = detalle_movimiento # 
		self.fecha = fecha # 

class Venta (Movimiento) :
	'''Clase para gestionar las ventas de la empresa, es una clase abstracta
'''
	def __init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha) : # 
		Movimiento.__init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha)		
		self.calcular_importe(self.importe,self.cantidad_productos)

	def calcular_importe (self,precio,cantidad) :
		self.total_movimiento=precio*cantidad
		


class VentaCredito (Venta):
	'''clase pendiente para version futura'''

	def __init__(self):
		pass
class VentaContado (Venta) :
	'''Clase que sirve para realizar las ventas al contado de productos de la empresa '''
	def __init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha,tipo_movimiento='venta') : # 	def __init__(self) :
		Venta.__init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha)
		self.tipo_movimiento=tipo_movimiento 
		pass
	def generar_detalle (self,tipo_insumo) :
		self.detalle_movimiento={1 : tipo_insumo,2 : self.cantidad_productos,3 : self.total_movimiento, 4 : self.fecha}	
		
		
class Insumo :
	'''Clase que sirve para gestinar la materia prima de la empresa
'''	
	#creamos un atributo de clase ya que para cada producto siempre se necesitan 100 gramos
	# de ese insumo
	insumo_producto=100
	def __init__(self,cantidad,precio,descripcion) :
		self.cantidad = cantidad # 
		self.precio = precio # 
		self.descripcion = descripcion #
		pass
	def restar_insumo(self,cantidad_a_restar):
		cantidad_a_restar=Insumo.insumo_producto*cantidad_a_restar
		self.cantidad=self.cantidad-cantidad_a_restar
	def sumar_insumo(self,cantidad_a_sumar):
		self.cantidad=self.cantidad+cantidad_a_sumar
		return True
	
	def verificar_existencia(self,cantidad_a_restar):
		cantidad_a_restar = Insumo.insumo_producto*cantidad_a_restar
		if cantidad_a_restar<=self.cantidad:
			return True
		else:
			return False
		


class Compra (Movimiento) :
	'''Clase para gestionar las compras de la empresa, es una clase abstracta'''
	def __init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha):
		Movimiento.__init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha)
		self.calcular_importe(self.importe,self.cantidad_productos)
		pass
	def calcular_importe (self,precio,cantidad) :
			self.total_movimiento=precio*cantidad
			pass


class CompraCredito (Compra):
	'''clase pendiente para version futura'''

	def __init__(self):
		pass


class CompraContado (Compra):
	'''Clase que sirve para realizar las compras al contado  de insumos de la empresa'''

	def __init__(self, importe, cantidad_productos, total_movimiento, detalle_movimiento, fecha,tipo_movimiento='compra'):
		Compra.__init__(self,importe,cantidad_productos,total_movimiento,detalle_movimiento,fecha)
		#para saber si es movimiento de compra usamos tipo_movimiento
		self.tipo_movimiento=tipo_movimiento

	def generar_detalle(self,tipo_insumo):

		self.detalle_movimiento={1 : tipo_insumo,2 : self.cantidad_productos,3 : self.total_movimiento, 4 : self.fecha}
		



