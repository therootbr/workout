
# Hugo Pablo Tomas de Araujo
# Marcus Levi Peixoto Jácome
# ICARO FELIPE LIMA LINHARES

class Contato:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
        self.prox = None

class Agenda:
    def __init__(self):
        self.ponta = None
        self._size = 0

    # consultar o tamanho da lista (item D)
    def __len__(self):
        return self._size

    def append(self, ctt):
        if self.ponta:
            # inserir contato em lista populada (ao final da lista)
            iterador = self.ponta
            while (iterador.prox):
                iterador = iterador.prox
            iterador.prox = ctt
        else:
            # primeira contato da agenda
            self.ponta = ctt
        self._size = self._size + 1

    def _getctt(self, index):
        iterador = self.ponta
        for i in range(index):
            if iterador:
                iterador = iterador.prox
            else:
                raise IndexError("list index out of range")  # return None
        return iterador

    def __getitem__(self, index):
        iterador = self._getctt(index)
        if iterador:
            return iterador.nome, iterador.telefone
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, nome, telefone): #não obrigatório na UI solicitada pela atividade, opção 8 (extra)
        iterador = self._getctt(index)
        if iterador:
            iterador.nome = nome
            iterador.telefone = telefone
        else:
            raise IndexError("list index out of range")

    def buscar(self, nome):
        iterador = self.ponta
        i = 0
        while (iterador):
            if iterador.nome == nome:
                return i
            iterador = iterador.prox
            i = i + 1
        raise ValueError("{} is not in list".format(nome))

    def inserir(self, index, nome, telefone): #não obrigatório na UI solicitada pela atividade, opção 7 (extra)
        ctt = Contato(nome, telefone)
        if index == 0:
            ctt.prox = self.ponta
            self.ponta = ctt
        else:
            iterador = self._getctt(index - 1)
            ctt.prox = iterador.prox
            iterador.prox = ctt
        self._size = self._size + 1

    def removerIndex(self, idx):
        if self.ponta == None:
            raise ValueError("{} is not in list".format(idx)) #raise é utilizado para detalhamento das ocorrencias de erro nas APIs, para casos mais simples usar print("deu erro (e qual erro)")
        aux = self.ponta

        if idx == 0: # se o contato for o unico da lista ou primeiro contato, desencadeia-o
            self.ponta = aux.prox
            aux = None

        for i in range(idx -1):#percorrer a lista a fim de achar o contato antecessor ao que será excluido
            aux = aux.prox
            if aux is None:
                break

        if aux is None:
            raise ValueError("{} is not in list".format(idx))
        if aux.prox is None:
            raise ValueError("{} is not in list".format(idx))

        prox = aux.prox.prox #armazenar a informação do sucessor do contato a ser excluido

        aux.prox = None #desencadear contato da lista
        aux.prox = prox #salvar a referencia do antecessor no sucessor do excluido
        self._size = self._size - 1 #diminuit o tamanho da lista
        return print("O contato foi excluido com sucesso!\n")


    def remover(self, nome):
        if self.ponta == None:
            raise ValueError("{} is not in list".format(nome))
        elif self.ponta.nome == nome:
            self.ponta = self.ponta.prox
            self._size = self._size - 1
            return True
        else:
            ancestor = self.ponta
            iterador = self.ponta.prox
            while (iterador):
                if iterador.nome == nome:
                    ancestor.prox = iterador.prox
                    iterador.prox = None
                    self._size = self._size - 1
                    return print("O contato foi excluido com sucesso!\n")
                ancestor = iterador
                iterador = iterador.prox
        raise ValueError("{} is not in list".format(nome))

    def __repr__(self):
        r = ""
        iterador = self.ponta
        i = 0  # EDIÇÃO UI 04 (INICIO CONTADOR FORA DO WHILE)
        while (iterador):
            i += 1  # EDIÇÃO UI 04 (soma com mais 1)
            r = r + "\nContato {} ".format(i) + "\nNome: " + str(iterador.nome) + "\nTelefone: " +str(iterador.telefone)+ "\n"
            iterador = iterador.prox
        return r

    def __str__(self):
        return self.__repr__()

agenda = Agenda()

def definirNome():
    return (input("Nome: "))

def definirIndice():
    return int((input("Posição: ")))


def definirTelefone():
    return (input("Telefone: "))

def criarCtt():
    nome = definirNome()
    telefone = definirTelefone()
    ctt = Contato(nome,telefone)
    print("O contato {} foi cadastrado com sucesso!\n".format(nome)) # EDIÇÃO UI 01
    agenda.append(ctt)

def escolherRemoverNome():
    nome = definirNome()
    agenda.remover(nome)

def escolherRemoverIndice():
    idx = definirIndice()
    agenda.removerIndex(idx)

def escolherBuscar():
    nome = definirNome()
    agenda.buscar(nome)

def escolherInserirIndice():
    idx = definirIndice()
    nome = definirNome()
    telefone = definirTelefone()
    agenda.inserir(idx, nome, telefone)

def escolherAlterarIndice():
    idx = definirIndice()
    nome = definirNome()
    telefone = definirTelefone()
    agenda.__setitem__(idx, nome, telefone)

# EDIÇÃO UI 02 (SIMPLIFICAÇÃO DO CÓDIGO)
def menu():
    while True:
        print("===== AGENDA TELEFÔNICA =====")
        print(" 1 - ADICIONAR CONTATO")
        print(" 2 - EXCLUIR CONTATO - PELO NOME")
        print(" 3 - EXCLUIR CONTATO - PELA POSIÇÃO")
        print(" 4 - LISTAR CONTATOS")
        print(" 5 - QUANTIDADE DE CONTATOS")
        print(" 6 - PROCURAR CONTATO")
        print(" 7 - ADICIONAR CONTATO - POSIÇÃO ESPECÍFICA")
        print(" 8 - EDITAR CONTATO")
        print(" 0 - SAIR")
        valor = int(input(">>"))

        if valor == 0:
            print("Saindo do programa...")
            break
        elif valor == 1:
            criarCtt()
        elif valor == 2:
            escolherRemoverNome()
        elif valor == 3:
            escolherRemoverIndice()
        elif valor == 4:
            print(agenda)
        elif valor == 5:
            print(agenda.__len__())
        elif valor == 6:
            escolherBuscar()
        elif valor == 7:
            escolherInserirIndice()
        elif valor == 8:
            escolherAlterarIndice()

        else:  # EDIÇÃO UI 03 (PREVENÇÃO DE ERROS)
            print("OPÇÃO INVÁLIDA, DIGITE UM NÚMERO CORRESPONDENTE AO MENU")

# nome1 = "hugo"
# telefone1 = "1234-5678"
# ctt1 = Contato(nome1,telefone1)
# agenda.append(ctt1)
#
# nome2 = "levi"
# telefone2 = "5678-1234"
# ctt2 = Contato(nome2,telefone2)
# agenda.append(ctt2)
#
# nome3 = "icaro"
# telefone3 = "5544-1234"
# ctt3 = Contato(nome3,telefone3)
# agenda.append(ctt3)
#
# nome4 = "maxi"
# telefone4 = "6699-1234"
# ctt4 = Contato(nome4,telefone4)
# agenda.append(ctt4)

#nome1 = "hugo"
# telefone1 = "1234-5678"
# ctt1 = Contato(nome1,telefone1)
#agenda.inserir(3, bidugo, 4564)
menu()