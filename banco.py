from cliente import Cliente
from conta import Conta

cliente1 = Cliente("Layane", "123456789", "123.456.789-00")
cliente2 = Cliente("João", "987654321", "987.654.321-00")

conta1 = Conta("001", cliente1, 1000)
conta2 = Conta("002", cliente2, 1500)

print(f"Nome: {cliente1.nome}")
print(f"Telefone: {cliente1.telefone}")
print(f"CPF: {cliente1.cpf}")

print(f"Nome: {cliente2.nome}")
print(f"Telefone: {cliente2.telefone}")
print(f"CPF: {cliente2.cpf}")

print(f"Saldo da Conta {conta1.numero}: R${conta1.consultar_saldo():.2f}")
print(f"Saldo da Conta {conta2.numero}: R${conta2.consultar_saldo():.2f}")
