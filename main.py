
from Animal import Animal
from Medico import Medico
from Atendimento import Atendimento
from datetime import date

listaAnimais = []
listaMedicos = []
listaAtendimentos = []

def buscarAnimal(nomeBusca):
    i = 0
    for animal in listaAnimais:
        if animal.get_nome() == nomeBusca:
            return animal, i
        i += 1
    return None, i

def buscarMedico(nomeBusca):
    i = 0
    for medico in listaMedicos:
        if medico.nome == nomeBusca:
            return medico, i
        i += 1
    return None, i


def menuAnimais():
    while True:
        print("\n\nBEM-VINDO AO SISTEMA DE ANIMAIS")
        print("Escolha uma opção: \n"
              "1 - 💾 Cadastrar Animal\n"
              "2 - 🔎 Listar Animais\n"
              "3 - ✏️ Alterar Animal\n"
              "4 - ❌ Excluir Animal\n"
              "0 - ⬅️ Voltar")
        escolha = input("Digite:")

        if escolha == "0":
            break
        elif escolha == "1":
            print("\n\n💾 CADASTRO DE ANIMAIS:")
            nome = input("Nome do Animal: ")
            especie = input("Espécie: ")
            idade = int(input("Idade: "))
            dono = input("Nome do Dono: ")

            novoAnimal = Animal(nome, especie, idade, dono)
            listaAnimais.append(novoAnimal)

        elif escolha == "2":
            print("\n\n🔎 LISTA DE ANIMAIS CADASTRADOS:")
            for animal in listaAnimais:
                print(animal)

        elif escolha == "3":
            print("\n\n✏️ ALTERAR INFORMAÇÕES SOBRE UM ANIMAL:")
            nome = input("Informe o Nome do Animal: ")
            animal, posicao = buscarAnimal(nome)
            if animal is None:
                print("Animal não encontrado!")
            else:
                especie = input("Nova Espécie: ")
                idade = int(input("Nova Idade: "))
                dono = input("Novo Dono: ")
                animal.especie = especie
                animal.idade = idade
                animal.set_dono(dono)

                listaAnimais[posicao] = animal
                print("Informações do animal alteradas com sucesso!")

        elif escolha == "4":
            print("\n\n❌ EXCLUIR ANIMAL:")
            nome = input("Informe o Nome do Animal: ")
            animal, posicao = buscarAnimal(nome)
            if animal is None:
                print("Animal não encontrado!")
            else:
                listaAnimais.pop(posicao)
                print("Animal excluído com sucesso!")

        else:
            print("Opção Inválida!")

def menuMedicos():
    while True:
        print("\n\nBEM-VINDO AO SISTEMA DE MÉDICOS VETERINÁRIOS")
        print("Escolha uma opção: \n"
              "1 - 💾 Cadastrar Médico\n"
              "2 - 🔎 Listar Médicos\n"
              "3 - ✏️ Alterar Médico\n"
              "4 - ❌ Excluir Médico\n"
              "0 - ⬅️ Voltar")
        escolha = input("Digite:")

        if escolha == "0":
            break
        elif escolha == "1":
            print("\n\n💾 CADASTRO DE MÉDICO:")
            nome = input("Nome do Médico: ")
            especialidade = input("Especialidade: ")
            crmv = input("CRMV: ")

            novoMedico = Medico(nome, especialidade, crmv)
            listaMedicos.append(novoMedico)

        elif escolha == "2":
            print("\n\n🔎 LISTA DE MÉDICOS CADASTRADOS:")
            for medico in listaMedicos:
                print(medico)

        elif escolha == "3":
            print("\n\n✏️ ALTERAR INFORMAÇÕES SOBRE UM MÉDICO:")
            nome = input("Informe o Nome do Médico: ")
            medico, posicao = buscarMedico(nome)
            if medico is None:
                print("Médico não encontrado!")
            else:
                especialidade = input("Nova Especialidade: ")
                crmv = input("Novo CRMV: ")
                medico.especialidade = especialidade
                medico.crmv = crmv

                listaMedicos[posicao] = medico
                print("Informações do médico alteradas com sucesso!")

        elif escolha == "4":
            print("\n\n❌ EXCLUIR MÉDICO:")
            nome = input("Informe o Nome do Médico: ")
            medico, posicao = buscarMedico(nome)
            if medico is None:
                print("Médico não encontrado!")
            else:
                listaMedicos.pop(posicao)
                print("Médico excluído com sucesso!")

        else:
            print("Opção Inválida!")

def menuAtendimentos():
    while True:
        print("\n\nBEM-VINDO AO SISTEMA DE ATENDIMENTOS")
        print("Escolha uma opção: \n"
              "1 - 🛠 Registrar Novo Atendimento\n"
              "0 - ⬅️ Voltar")
        escolha = input("Digite:")

        if escolha == "0":
            break
        elif escolha == "1":
            print("\n\n🛠 REGISTRO DE ATENDIMENTO:")
            nome_animal = input("Nome do Animal: ")
            animal, _ = buscarAnimal(nome_animal)
            if animal is None:
                print("Animal não encontrado!")
                continue

            nome_medico = input("Nome do Médico: ")
            medico, _ = buscarMedico(nome_medico)
            if medico is None:
                print("Médico não encontrado!")
                continue

            descricao = input("Descrição do Atendimento: ")
            data_atendimento = date.today()

            novoAtendimento = Atendimento(animal, medico, data_atendimento, descricao)
            listaAtendimentos.append(novoAtendimento)

            print("Atendimento registrado com sucesso!")
            print(novoAtendimento)

        else:
            print("Opção Inválida!")

while True:
    print("\n\nBEM-VINDO AO SISTEMA DE GESTÃO DA CLÍNICA VETERINÁRIA")
    print("Escolha uma opção: \n"
          "1 - 👤 Gestão de Animais\n"
          "2 - 👨‍⚕️ Gestão de Médicos\n"
          "3 - 📝 Gestão de Atendimentos\n"
          "0 - ⬅️ Sair")
    escolha = input("Digite:")

    if escolha == "0":
        break
    elif escolha == "1":
        menuAnimais()
    elif escolha == "2":
        menuMedicos()
    elif escolha == "3":
        menuAtendimentos()
    else:
        print("Opção Inválida!")

print("\nSistema encerrado. Obrigado por utilizar a gestão da clínica veterinária!")
