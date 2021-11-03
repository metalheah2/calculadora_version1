from calculadora import *

class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	def __init__(self,*args,**kwargs):
		QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
		_translate=QtCore.QCoreApplication.translate
		self.setupUi(self)
		
		self.mostrar_resultado.setText("")
		#Numeros
		self.boton_0.pressed.connect(self.todos)
		self.boton_1.pressed.connect(self.todos)
		self.boton_2.pressed.connect(self.todos)
		self.boton_3.pressed.connect(self.todos)
		self.boton_4.pressed.connect(self.todos)
		self.boton_5.pressed.connect(self.todos)
		self.boton_6.pressed.connect(self.todos)
		self.boton_7.pressed.connect(self.todos)
		self.boton_8.pressed.connect(self.todos)
		self.boton_9.pressed.connect(self.todos)
		#Operadores
		self.boton_multi.clicked.connect(self.multiplicacion)
		self.boton_div.clicked.connect(self.division)
		self.boton_mas.clicked.connect(self.suma)
		self.boton_menos.clicked.connect(self.resta)
		self.boton_igual.clicked.connect(self.resultado)
		#Preset
		self.boton_ce.clicked.connect(self.reset)
		self.boton_del.clicked.connect(self.delete)
	#Funciones
	def multiplicacion(self):
		item2=self.mostrar_resultado.text()
		self.mostrar_resultado.setText(str(item2)+str("x"))
	def division(self):
		item2=self.mostrar_resultado.text()
		self.mostrar_resultado.setText(str(item2)+str("/"))
	def suma(self):
		item2=self.mostrar_resultado.text()
		self.mostrar_resultado.setText(str(item2)+str("+"))
	def resta(self):
		item2=self.mostrar_resultado.text()
		self.mostrar_resultado.setText(str(item2)+str("-"))
	#Funcion Resultado
	def resultado(self):
		operacion=self.mostrar_resultado.text()
		signo_mult=operacion.find("x")
		signo_div=operacion.find("/")
		signo_sum=operacion.find("+")
		signo_res=operacion.find("-")
		def digitos(signo):
			cantidad=len(operacion)
			num1_cant=operacion[0:signo]
			num2_cant=operacion[signo+1:cantidad]
			return num1_cant,num2_cant
		def resultado_operacion(res_1,ope_1):
			self.mostrar_resultado.setText(str(res_1))
			self.mostrar_operaciones.setText(str(operacion))
		if(signo_mult>=1):
			num1_cant,num2_cant=digitos(signo_mult)
			res_1=int(num1_cant)*int(num2_cant)
			resultado_operacion(res_1,operacion)
		elif(signo_div>=1):
			num1_cant,num2_cant=digitos(signo_div)
			res_1=int(num1_cant)/int(num2_cant)
			resultado_operacion(res_1,operacion)
		elif(signo_sum>=1):
			num1_cant,num2_cant=digitos(signo_sum)
			res_1=int(num1_cant)+int(num2_cant)
			resultado_operacion(res_1,operacion)
		elif(signo_res>=1):
			num1_cant,num2_cant=digitos(signo_res)
			res_1=int(num1_cant)-int(num2_cant)
			resultado_operacion(res_1,operacion)
	#Funcion Numeros
	def todos(self):
		item=[0,1,2,3,4,5,6,7,8,9]
		item[0]=self.boton_0.isDown()
		item[1]=self.boton_1.isDown()
		item[2]=self.boton_2.isDown()
		item[3]=self.boton_3.isDown()
		item[4]=self.boton_4.isDown()
		item[5]=self.boton_5.isDown()
		item[6]=self.boton_6.isDown()
		item[7]=self.boton_7.isDown()
		item[8]=self.boton_8.isDown()
		item[9]=self.boton_9.isDown()
		for valor in range(0,10):
			if(item[valor]==1):
				item2=self.mostrar_resultado.text()
				self.mostrar_resultado.setText(str(item2)+str(valor))
				
	def reset(self):
		self.mostrar_resultado.setText("")
		self.mostrar_operaciones.setText("0")
	def delete(self):
		operacion=self.mostrar_resultado.text()
		cantidad=len(operacion)
		mensaje=operacion[0:cantidad-1]
		self.mostrar_resultado.setText(mensaje)
		
if __name__=="__main__":
	#crear_tabla
	app=QtWidgets.QApplication([])
	window=MainWindow()
	window.show()
	app.exec_()