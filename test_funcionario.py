from funcionario import Funcionario
from gerente import Gerente

funcionario1 = Funcionario(nome="Layane", cpf="107.088.363.80", salario=10000)
gerente1 = Gerente(nome="Arthur", cpf="088.789.450.20", salario=20000,
                   senha="123", qtd_funcionarios=1)

print(f"Atributos do funcionário: {vars(funcionario1)}")
print(f"Atributos do gerente: {vars(gerente1)}")