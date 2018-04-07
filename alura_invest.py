from conta import Conta
from datas import Data

conta1 = Conta(1, "Fulano", 0.0)
conta2 = Conta(2, "Beltrano", 0.0)
conta3 = Conta(3, "Siclano", 0.0, 2000.0)

conta1.extrato()
conta1.deposita(50.0)
conta1.extrato()


data = Data(21, 11, 2007)
data.formatada()

conta2.extrato()
print("Transferencia de Fulano para Beltrano")
conta1.transfere(20.0, conta2)
conta1.extrato()
conta2.extrato()