#CRIADO POR:
## HUGO PABLO TOMAS DE ARAUJO - 20201044110032
## ICARO FELIPE LIMA LINHARES - 20201044110015
## MARCUS LEVI PEIXOTO JACOME - 20201044110017

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        #insere um elemento na pilha
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1

    def pop(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node.data
        raise IndexError("Lista vazia")

    #metodo usado para imprimir a pilha de cima para baixo
    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data)
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

pilha = Stack()

def splitWord(str):
    return [char for char in str]

def inserirPalavra(str):
    nStr = splitWord(str)
    for i in nStr:
        pilha.push(i)
    print(pilha, end="")
    return "Done. Reversed."


def obterPalavra():
    str = input("Digite uma palavra")
    return str

palavraReversa = inserirPalavra(obterPalavra())
