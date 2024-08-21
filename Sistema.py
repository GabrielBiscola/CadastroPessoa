# 1- Pessoa Fisica / 2 - Pessoa Juridica / 3 - Sair
# 1- Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Sair
# 1- Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Sair

from datetime import date, datetime
from Pessoa import PessoaFisica, Endereco, PessoaJuridica


def main():
    lista_pf = []
    lista_pj = []
    while True:
        opcao = int(input("Escolha uma opcao: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair"))
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1- Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Remover Pessoa Fisica / 4 - Editar Cadastro / 0 - Sair"))
                # Cadastrar uma Pessoa Fisica
                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica")
                    novapf.cpf = input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mensal (use somente numeros)"))

                    data_nascimento = input("Digite a data de nascimento (dd/MM/aaaa): ")
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue

                    novo_end_pf.logradouro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o numero: ")
                    end_comercial = input("Este endereco é comercial? s/n") # Solicitar se o endereco eh comercial
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!!")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print(f"Digite - para sair: ")
                            input()
                    else:
                        print("Lista vazia")

                elif opcao_pf == 3:
                    cpf_para_remover = input("Digite o CPF que você quer remover: ")

                    pessoa_encontrada = False

                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_remover:
                            lista_pf.remove(cada_pf)
                            pessoa_encontrada = True
                            print("Pessoa fisica removida!")

                            break
                    if not pessoa_encontrada:
                        print("Pessoa não encontrada")

                elif opcao_pf == 4:
                    cpf_para_editar = input("Digite o CPF que você quer editar")
                    for cada_pf in lista_pf:
                        if cada_pf.cpf == cpf_para_editar:
                            cpf_editar = cada_pf
                            pessoa_encontrada = True

                            break

                    if not pessoa_encontrada:
                        print("Pessoa não encontrada")
                    else:
                        while True:
                            opcao_editar = int(input("O que você quer atualizar: 1- Nome / 2 - CPF / 3 - Endereço / 4 - Rendimento / 0 - Sair"))
                            if opcao_editar == 1:
                                cpf_editar.nome = input("Digite o nome da pessoa fisica")
                            
                            elif opcao_editar == 2:
                                cpf_editar.cpf = int(input("Tá maluco, vai editar o CPF? (digite o novo CPF)"))
                                


                            elif opcao_editar == 3:
                                novo_end_pf = Endereco()
                                novo_end_pf.logradouro = input("Digite o logradouro: ")
                                novo_end_pf.numero = input("Digite o numero: ")
                                end_comercial = input("Este endereco é comercial? s/n") 
                                novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == 'S'
                                cpf_editar.endereco = novo_end_pf
                                print("Endereço atualizado")
                            
                            elif opcao_editar == 4:
                                cpf_editar.rendimento = float(input("Digite o rendimento mensal (use somente numeros)"))
                                print("Rendimento atualizado")
                            
                            elif opcao_editar == 0:
                                print("Modo de edição finalizado")
                                break # Falta o do CNPJ
                        
                elif opcao_pf == 0: 
                    print("Voltando ao menu anterior")
                    break
                else: 
                    print("Opção inválida, por favor digite uma das opções inidicadas: ")

        elif opcao == 2: 
            while True:
                opcao_pj = int(input("Escolha uma opcao: 1- Cadastrar Pessoa Juridica / 2 - Listar Pessoa Juridica / 3 - Remover Pessoa Juridica / 4 -Editar Cadastro / 0 - Sair"))
                if opcao_pj == 1:
                    novapj = PessoaJuridica()
                    novo_end_pj = Endereco()

                    novapj.nome = input("Digite o nome fantasia da pessoa juridica")
                    novapj.cnpj = input("Digite o CNPJ")
                    novapj.rendimento = float(input("Digite o rendimento mensal (use somente numeros)"))

                    data_abertura = input("Digite a data de abertura (dd/MM/aaaa): ")
                    novapj.dataAbertura = datetime.strptime(data_abertura, '%d/%m/%Y').date()
                    idade = (date.today() - novapj.dataAbertura).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue

                    novo_end_pj.logradouro = input("Digite o logradouro: ")
                    novo_end_pj.numero = input("Digite o numero: ")
                    end_comercialpj = input("Este endereco é comercial? s/n") # Solicitar se o endereco eh comercial
                    novo_end_pj.endereco_Comercial = end_comercialpj.strip().upper() == 'S'

                    novapj.endereco = novo_end_pj

                    lista_pj.append(novapj)

                    print("Cadastro realizado com sucesso!!!")
                    
                elif opcao_pj == 2:
                    if lista_pj:
                        for cada_pj in lista_pj:
                            print(f"Nome Fantasia: {cada_pj.nome}")
                            print(f"CNPJ: {cada_pj.cnpj}")
                            print(f"Endereco: {cada_pj.endereco.logradouro}, {cada_pj.endereco.numero}")
                            print(f"Data Abertura: {cada_pj.dataAbertura.strftime('%d/%m/%Y')}")
                            print(f"Imposto a ser pago: {cada_pj.calcular_imposto(cada_pj.rendimento)}")
                            print(f"Digite - para sair: ")
                            input()
                    else:
                        print("Lista vazia")

                elif opcao_pj == 3:
                    cnpj_para_remover = input("Digite o CNPJ que você quer remover: ")

                    pessoa_encontrada = False

                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_para_remover:
                            lista_pj.remove(cada_pj)
                            pessoa_encontrada = True
                            print("Pessoa juridica removida!")

                            break
                        else:
                            print("Empresa não encontrada")

                elif opcao_pf == 4:
                    cnpj_para_editar = input("Digite o CNPJ que você quer editar")
                    for cada_pj in lista_pj:
                        if cada_pj.cnpj == cnpj_para_editar:
                            cnpj_editar = cada_pj
                            pessoa_encontrada = True

                            break

                    if not pessoa_encontrada:
                        print("Pessoa não encontrada")
                    else:
                        while True:
                            opcao_editar = int(input("O que você quer atualizar: 1- Nome / 2 - CNPJ / 3 - Endereço / 4 - Rendimento / 0 - Sair"))
                            if opcao_editar == 1:
                                cnpj_editar.nome = input("Digite o nome da pessoa fisica")
                            
                            elif opcao_editar == 2:
                                cnpj_editar.cnpj = int(input("Tá maluco, vai editar o CNPJ? (digite o novo CNPJ)"))
                                
                            elif opcao_editar == 3:
                                novo_end_pj = Endereco()
                                novo_end_pj.logradouro = input("Digite o logradouro: ")
                                novo_end_pj.numero = input("Digite o numero: ")
                                end_comercial = input("Este endereco é comercial? s/n") 
                                novo_end_pj.endereco_Comercial = end_comercial.strip().upper() == 'S'
                                cnpj_editar.endereco = novo_end_pj
                                print("Endereço atualizado")
                            
                            elif opcao_editar == 4:
                                cnpj_editar.rendimento = float(input("Digite o rendimento mensal (use somente numeros)"))
                                print("Rendimento atualizado")
                            
                            elif opcao_editar == 0:
                                print("Modo de edição finalizado")
                                break # Falta o do CNPJ

                elif opcao_pj == 0: 
                    print("Voltando ao menu anterior")
                    break
                else: 
                    print("Opção inválida, por favor digite uma das opções inidicadas: ")

        elif opcao == 0:
            print("Obrigado por utilizar o nome sistema! Valeu!")
            break
        else: 
            print("Opção inválida, por favor digite uma das opções válidas!")

if __name__ == "__main__":
    main()
                            
