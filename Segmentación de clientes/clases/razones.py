import clases.cliente

class Razon:
    def __init__(self, evento, cliente) -> None:
        self.razon = self.resolver(evento, cliente)

    @staticmethod
    def resolver(evento, obj) -> str:
        tipo_evento = evento['tipo']
        match tipo_evento:
            case 'RETIRO_EFECTIVO_CAJERO_AUTOMATICO':
                return RazonRetiroEfectivo.validacion(evento, obj.cuenta)
            case 'ALTA_TARJETA_CREDITO':
                return RazonAltaTarjetaCredito.validacion(evento, obj)
            case 'ALTA_CHEQUERA':
                return RazonAltaChequera.validacion(evento, obj)
            case 'COMPRA_DOLAR':
                return RazonCompraDolar.validacion(evento, obj)
            case 'TRANSFERENCIA_ENVIADA':
                return RazonTransferenciaEnviada.validacion(evento, obj.cuenta)
            case 'TRANSFERENCIA_RECIBIDA':
                return RazonTransferenciaRecibida.validacion(evento, obj.cuenta)

class RazonRetiroEfectivo:
    @staticmethod
    def validacion(evento, cuenta):
        if evento['monto'] < cuenta.limite_extraccion_diario:
            if not evento['monto'] <= evento['cupoDiarioRestante']:
                return f"La cantidad supera el cupo diario de retiros, puede retirar hasta ${evento['cupoDiarioRestante']}. "
            elif evento['monto'] > evento['saldoEnCuenta']:
                return f"No tiene fondos suficientes"
        else:
            return f"Excede el monto de máximo de ${cuenta.limite_extraccion_diario}"

class RazonAltaChequera:
    @staticmethod
    def validacion(evento, cliente):
        if not cliente.puede_crear_chequera(evento['totalChequerasActualmente']):
            if evento['totalChequerasActualmente'] == 0:
                return f"El cliente no puede crear chequeras"
            else:
                return f"El cliente no puede crear más chequeras"

class RazonAltaTarjetaCredito:
    @staticmethod
    def validacion(evento, cliente):
        if not cliente.puede_crear_tarjeta_de_credito(evento['totalTarjetasDeCreditoActualmente']):
            if evento['totalTarjetasDeCreditoActualmente'] == 0:
                return f"El cliente no puede crear tarjetas de crédito"
            else:
                return f"El cliente no puede crear más tarjetas de crédito"

class RazonCompraDolar:
    @staticmethod
    def validacion(evento, cliente):
        if not cliente.puede_comprar_dolar:
            return f"El cliente no puede comprar dolares"
        else:
            return f"No puede realizar la compra porque el monto de ${evento['monto']} supera elsaldo de la cuenta"

class RazonTransferenciaEnviada:
    @staticmethod
    def validacion(evento, cuenta):
        if cuenta.costo_transferencia == None or evento['monto'] > cuenta.costo_transferencia:
            return f"El monto ${evento['monto']} supera el saldo de la cuenta"

class RazonTransferenciaRecibida:
    @staticmethod
    def validacion(evento, cuenta):
        if cuenta.limite_transferencia_recibida == None or evento['monto'] > cuenta.limite_transferencia_recibida:
            return f"No puede recibir un monto de ${evento['monto']} sin previo sin aviso"