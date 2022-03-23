class Auto:
	cantidadCreados = 0
	def __init__(self, modelo, precio, asientos, marca, motor, registro):
		self.modelo = modelo
		self.precio = precio
		self.asientos = asientos 
		self.marca = marca
		self.motor = motor 
		self.registro = registro
	
	#método que determina la cantidad de objetos tipo Asiento
	def cantidadAsientos(self):
		total = 0
		for i in self.asientos:
			verificar = type(i) == Asiento
			if verificar == True:
				total += 1
		return total

	#método que verifica la coincidencia del registro entre las partes
	def verificarIntegridad(self):
		for i in self.asientos:
			if i != None:
				if self.registro == i.registro and self.registro == self.motor.registro:
					return "Auto original"
				else:
					return "Las piezas no son originales"


class Asiento:
	def __init__(self,color,precio,registro):
		self.color = color
		self.precio = precio
		self.registro = registro

	#método que permite cambiar el color del asiento, pero restringe valores
	def cambiarColor(self,color):
		colores = ["rojo","verde","amarillo","negro","blanco"]
		if color not in colores:
			pass
		else:
			self.color = color


class Motor:
	def __init__(self,numeroCilindros,tipo,registro):
		self.numeroCilindros = numeroCilindros
		self.tipo = tipo
		self.registro = registro

	#método que cambia el registro del motor
	def cambiarRegistro(self,registro):
		self.registro = registro

	#método que asigna el tipo de motor, alternativa binaria
	def asignarTipo(self,tipo):
		tipos = ["electrico","gasolina"]
		if tipo not in tipos:
			pass
		else:
			self.tipo = tipo
			
