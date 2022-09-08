from abc import ABC, abstractmethod
from clases.cuenta import *
from clases.direccion import Direccion

class Cliente(ABC):
    def __init__(self, datos, datos_cuenta) -> None:
        self.cuenta = Cuenta(datos_cuenta, datos['transacciones'], self)
        self.direccion = Direccion(datos['direccion'])
        self.nombre = datos['nombre']
        self.apellido = datos['apellido']
        self.numero = datos['numero']
        self.dni = datos['dni']

    def get_cuenta(self):
        return self.cuenta

    @abstractmethod
    def puede_crear_chequera(self, cant_chequeras) -> bool:
        pass

    @abstractmethod
    def puede_crear_tarjeta_de_credito(self, cant_tarjetas) -> bool:
        pass

    @abstractmethod
    def puede_comprar_dolar(self) -> bool:
        pass

    @abstractmethod
    def posee_cuenta_corriente(self) -> bool:
        pass

    def costo_transferencia(self, monto: int) -> int:
        pass
