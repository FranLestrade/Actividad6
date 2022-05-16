class Cuenta:
      def __init__(self,titular,cantidad):
         self.titular= titular
         self.cantidad= cantidad
     
      def mostrar(self):
        print("Bienvenid@. Usted es", self.titular,"y tiene un balance de", self.cantidad, ".")   

      def ingresar(self, a):
        if a < 0:
          print("El monto ingresado no es correcto. Inténtelo de nuevo.")
        else:
          print("Ha ingresado dinero con éxito. Su nuevo balance es de", self.cantidad + a)
          value= self.cantidad + a
      def retirar(self,b):
        print("Dinero retirado con éxito. Su balance ahora es de", self.cantidad - b)    
        
 
persona=Cuenta("Franco", 2000)
persona.mostrar()
persona.ingresar(-30)
persona.ingresar(2000)
persona.retirar(2500)