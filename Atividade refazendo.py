# Sala : 93313 , Turma : Vespertino
# João Victor Agapio Modesto Mendes , Bruno Santos.

import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Limpar o console
os.system("cls||clear")

# Criar banco de dados
BANCO = create_engine("sqlite:///RhSystem.db")

# Criar sessão
Session = sessionmaker(bind=BANCO)
session = Session()

# Criar base
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id_do_funcionario = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    cpf = Column("cpf", String)  # Mudado para String
    setor = Column("setor", String)
    funcao = Column("funcao", String)
    salario = Column("salario", Integer)
    telefone = Column("telefone", String)

    def __init__(self, nome: str, cpf: str, setor: str, funcao: str, salario: int, telefone: str):
        self.nome = nome
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

# Criar tabelas
Base.metadata.create_all(bind=BANCO)

def salvar_funcionario(nomee, cpff, setorr, funcaoo, salarioo, telefonee):
    funcionario = Funcionario(nome=nomee, cpf=cpff, setor=setorr, funcao=funcaoo, salario=salarioo, telefone=telefonee)
    session.add(funcionario)
    session.commit()
    print("Salvo com sucesso!")

def listar_todos_funcionarios():
    print("\nExibindo todos os funcionários do banco de dados.")
    lista_funcionario = session.query(Funcionario).all()

    for funcionarios in lista_funcionario:
        print(f"Nome: {funcionarios.nome}, CPF: {funcionarios.cpf}, Setor: {funcionarios.setor}, Função: {funcionarios.funcao}")

def pesquisar_um_funcionario(cpf):
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        print(f"Nome: {funcionario.nome}, CPF: {funcionario.cpf}, Setor: {funcionario.setor}, Função: {funcionario.funcao}")
    else:
        print("Funcionário não encontrado.")

def atualizar_funcionario(cpf):
    print("\nAtualizando dados do funcionário.")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        funcionario.nome = input("Digite seu nome: ")
        funcionario.cpf = input("Digite seu cpf: ")
        funcionario.setor = input("Digite seu setor: ")
        funcionario.funcao = input("Digite sua função: ")
        funcionario.salario = int(input("Digite seu salário: "))
        funcionario.telefone = input("Digite seu telefone: ")

        session.commit()
        print("Dados atualizados com sucesso!")
    else:
        print("Funcionário não encontrado.")

def excluir_funcionario(cpf):
    print("\nExcluindo um funcionário.")
    funcionario = session.query(Funcionario).filter_by(cpf=cpf).first()
    if funcionario:
        session.delete(funcionario)
        session.commit()
        print(f"{funcionario.cpf} excluído com sucesso.")
    else:
        print("Funcionário não encontrado.")

while True:
    print("""
        === Sistema RH ===
    1 - Adicionar funcionário
    2 - Consultar um funcionário
    3 - Atualizar os dados de um funcionário
    4 - Excluir um funcionário
    5 - Listar todos os funcionários
    0 - Sair do sistema.
    """)
    opcao = int(input("Digite a opção: "))
    match opcao:
        case 1:
            nomee = input("Digite seu nome: ")
            cpff = int(input("Digite seu cpf: "))
            setorr = input("Digite seu setor: ")
            funcaoo = input("Digite sua função: ")
            salarioo = int(input("Digite seu salário: "))  
            telefonee = int(input("Digite seu telefone: "))
            salvar_funcionario(nomee, cpff, setorr, funcaoo, salarioo, telefonee)
        case 2:
            cpf = input("Digite seu cpf: ")
            pesquisar_um_funcionario(cpf)
        case 3:
            cpf = input("Digite seu cpf: ")
            atualizar_funcionario(cpf)
        case 4:
            cpf = input("Digite seu cpf: ")
            excluir_funcionario(cpf)
        case 5:
            listar_todos_funcionarios()
        case 0:
            print("Sistema fechado.")
            break
        case _:
            print("ERRO")
          