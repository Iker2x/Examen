from abc import ABC, abstractmethod

class Empleado_o12(ABC):
    def __init__(self, RFC, apellidos, nombres):
        self.RFC = RFC
        self.apellidos = apellidos
        self.nombres = nombres

    @abstractmethod
    def calcular_sueldo_neto(self):
        pass

    def mostrar_info(self):
        print(f"RFC: {self.RFC}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Nombres: {self.nombres}")

class EmpleadoVendedor_o12(Empleado_o12):
    def __init__(self, RFC, apellidos, nombres, monto_vendido, tasa_comision):
        super().__init__(RFC, apellidos, nombres)
        self.monto_vendido = monto_vendido
        self.tasa_comision = tasa_comision

    def calcular_ingresos(self):
        return self.monto_vendido * self.tasa_comision

    def calcular_bonificacion(self):
        ingresos = self.calcular_ingresos()
        if self.monto_vendido < 1000:
            return 0
        elif 1000 <= self.monto_vendido <= 5000:
            return 0.05 * ingresos
        else:
            return 0.10 * ingresos

    def calcular_descuento(self):
        ingresos = self.calcular_ingresos()
        if ingresos < 1000:
            return 0.11 * ingresos
        else:
            return 0.15 * ingresos

    def calcular_sueldo_neto(self):
        ingresos = self.calcular_ingresos()
        bonificacion = self.calcular_bonificacion()
        descuento = self.calcular_descuento()
        return ingresos + bonificacion - descuento

class EmpleadoPermanente_o12(Empleado_o12):
    def __init__(self, RFC, apellidos, nombres, sueldo_base, numero_seguro_social):
        super().__init__(RFC, apellidos, nombres)
        self.sueldo_base = sueldo_base
        self.numero_seguro_social = numero_seguro_social
    def get_sueldo_base(self):
        return self.sueldo_base
    def calcular_descuento(self):
        return 0.11 * self.sueldo_base
    def calcular_sueldo_neto(self):
        return self.sueldo_base - self.calcular_descuento()

def main():
    try:
        vendedor = EmpleadoVendedor_o12("RFC123", "Ortega", "Luis", 3000, 0.05)
        vendedor.mostrar_info()
        print("Sueldo neto vendedor: ${:.2f}".format(vendedor.calcular_sueldo_neto()))
        permanente = EmpleadoPermanente_o12("RFC456", "Perez", "Ana", 2000, "SS12345")
        permanente.mostrar_info()
        print("Sueldo neto permanente: ${:.2f}".format(permanente.calcular_sueldo_neto()))
        if permanente.get_sueldo_base() < 150:
            raise Exception("El sueldo base no puede ser menor a 150 pesos.")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
